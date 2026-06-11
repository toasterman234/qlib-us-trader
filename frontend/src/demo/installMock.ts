// DEMO mode (VITE_DEMO=1): intercept the API so the UI runs with sample data
// and no backend. Wraps window.fetch for /api/v1/* routes and neutralises the
// realtime WebSocket so it doesn't spam reconnect attempts. No-op in normal
// builds — installMock() is only called when import.meta.env.VITE_DEMO === '1'.

import { MOCK } from './mockData'

function json(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function route(path: string): Response | null {
  // Most specific routes first.
  if (path === '/dashboard/summary') return json(MOCK.dashboardSummary)
  if (path === '/factors' || path.startsWith('/factors?')) return json(MOCK.factorList)
  if (path === '/jobs' || path.startsWith('/jobs?')) return json(MOCK.jobs)

  if (path.startsWith('/backtest/walk-forward')) {
    const sub = path.replace('/backtest/walk-forward', '').split('?')[0]
    if (sub === '/available-weeks') return json(MOCK.availableWeeks)
    if (sub === '/summary') return json(MOCK.summary)
    if (sub === '' || sub === '/') return json(MOCK.backtestList)
    if (/^\/\d+$/.test(sub)) return json(MOCK.backtestDetail) // /{id}
  }

  // Anything else: a benign empty object so callers don't error out.
  return json({})
}

export function installMock() {
  const origFetch = window.fetch.bind(window)

  window.fetch = ((input: RequestInfo | URL, init?: RequestInit): Promise<Response> => {
    const url = typeof input === 'string' ? input : input instanceof URL ? input.href : input.url
    const idx = url.indexOf('/api/v1')
    if (idx !== -1) {
      const path = url.slice(idx + '/api/v1'.length)
      const res = route(path)
      if (res) return Promise.resolve(res)
    }
    return origFetch(input as RequestInfo, init)
  }) as typeof window.fetch

  // Silence the realtime socket — there's no backend in demo mode.
  class NoopWebSocket {
    readyState = 3 // CLOSED
    onopen: (() => void) | null = null
    onclose: (() => void) | null = null
    onerror: (() => void) | null = null
    onmessage: ((e: MessageEvent) => void) | null = null
    constructor(_url: string) {}
    send() {}
    close() {}
    addEventListener() {}
    removeEventListener() {}
  }
  // @ts-expect-error - intentional stub for demo mode
  window.WebSocket = NoopWebSocket

  // eslint-disable-next-line no-console
  console.info('[demo] sample-data mode active — API calls are mocked')
}
