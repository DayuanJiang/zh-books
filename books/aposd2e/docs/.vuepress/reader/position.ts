import { nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { onContentUpdated } from 'vuepress/client'
import { useReader } from './state'

// Set by the redirect in config.ts when opening the book's home page reopens the last chapter read.
const resumeFlag = 'aposd-reader-resume'

// Reading position: the topmost block of #content on screen, saved per chapter route. Opening the book from
// its home page returns to it and shows a short notice with a way back to the chapter start.
export function useReadingPosition() {
  const route = useRoute()
  const { preferences, init } = useReader()
  const resumed = ref<{ percent: number } | null>(null)
  let ready = false
  let saveTimer = 0
  let hideTimer = 0
  let restoredScroll: number | null = null
  let stopAligning = () => {}

  const header = () => document.querySelector('.reader-topbar')?.getBoundingClientRect().height || 52
  const blocks = () => [...document.querySelectorAll<HTMLElement>('#content > *')]
  const percent = () => {
    const total = document.documentElement.scrollHeight - innerHeight
    return total > 0 ? Math.round(Math.min(100, Math.max(0, scrollY / total * 100))) : 0
  }

  function save() {
    clearTimeout(saveTimer)
    // Only chapters are resumed (the home page is not), and right after a restore the end of the previous
    // block shows above the restored one: saving then would step back one block on every reopen.
    if (!ready || route.path !== preferences.lastRoute ||
      (restoredScroll !== null && Math.abs(scrollY - restoredScroll) < 2)) return
    const limit = header() + 8
    const index = blocks().findIndex((node) => node.getClientRects().length && node.getBoundingClientRect().bottom > limit)
    preferences.position = { route: route.path, index, percent: percent() }
  }
  function schedule() {
    clearTimeout(saveTimer)
    saveTimer = window.setTimeout(save, 400)
  }
  function hidden() { if (document.hidden) save() }

  async function restore(saved: { index: number, percent: number }) {
    restoredScroll = scrollY  // no saving until the block is back in place
    resumed.value = saved.percent >= 2 ? { percent: saved.percent } : null
    await nextTick()
    // The block starts below the notice, so its first line is not covered.
    const toast = document.querySelector('.reader-resume-toast')
    const offset = toast ? toast.getBoundingClientRect().bottom + 16 : header() + 20
    const align = () => {
      const block = blocks()[saved.index]
      const top = block ? scrollY + block.getBoundingClientRect().top - offset
        : saved.percent / 100 * (document.documentElement.scrollHeight - innerHeight)
      window.scrollTo({ top: Math.max(0, top), behavior: 'instant' })
      restoredScroll = scrollY
    }
    align()
    // Diagrams and figures that finish loading later push the text down: keep the block in place for a few
    // seconds, until the reader scrolls or clicks.
    const observer = new ResizeObserver(align)
    const content = document.getElementById('content')
    if (content) observer.observe(content)
    const events = ['wheel', 'touchstart', 'keydown', 'pointerdown']
    stopAligning = () => { observer.disconnect(); events.forEach((name) => removeEventListener(name, stopAligning)) }
    events.forEach((name) => addEventListener(name, stopAligning, { passive: true }))
    window.setTimeout(stopAligning, 4000)
    hideTimer = window.setTimeout(() => { resumed.value = null }, 6000)
  }
  function backToStart() {
    stopAligning()
    window.scrollTo({ top: 0, behavior: 'instant' })
    resumed.value = null
  }

  watch(() => route.path, () => { resumed.value = null; restoredScroll = null })
  onContentUpdated((reason) => { if (reason !== 'beforeUnmount') nextTick(save) })
  onMounted(() => {
    init()
    let flagged = false
    try { flagged = sessionStorage.getItem(resumeFlag) === '1'; sessionStorage.removeItem(resumeFlag) } catch {}
    ready = true
    const saved = preferences.position
    if (flagged && saved && saved.route === route.path) restore({ ...saved })
    else save()
    window.addEventListener('scroll', schedule, { passive: true })
    window.addEventListener('pagehide', save)
    document.addEventListener('visibilitychange', hidden)
  })
  onBeforeUnmount(() => {
    clearTimeout(saveTimer)
    clearTimeout(hideTimer)
    stopAligning()
    window.removeEventListener('scroll', schedule)
    window.removeEventListener('pagehide', save)
    document.removeEventListener('visibilitychange', hidden)
  })
  return { resumed, backToStart }
}
