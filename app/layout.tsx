import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: '响应式网站',
  description: '一个可以在手机浏览器上完美展示的响应式网站',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh">
      <body>{children}</body>
    </html>
  )
} 