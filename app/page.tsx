export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-800 mb-2">
            欢迎访问我的网站
          </h1>
          <p className="text-gray-600">
            这是一个响应式网站，在手机和电脑上都能完美展示
          </p>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* 特性卡片 1 */}
          <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
            <h2 className="text-xl font-semibold text-primary mb-3">响应式设计</h2>
            <p className="text-gray-600">
              完美适配各种屏幕尺寸，从手机到桌面设备都能获得最佳体验。
            </p>
          </div>

          {/* 特性卡片 2 */}
          <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
            <h2 className="text-xl font-semibold text-secondary mb-3">快速加载</h2>
            <p className="text-gray-600">
              优化的性能确保网站快速加载，提供流畅的用户体验。
            </p>
          </div>

          {/* 特性卡片 3 */}
          <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
            <h2 className="text-xl font-semibold text-primary mb-3">现代技术</h2>
            <p className="text-gray-600">
              使用最新的Web技术构建，确保最佳性能和可维护性。
            </p>
          </div>
        </section>

        <section className="mt-12">
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">联系我们</h2>
            <form className="space-y-4">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                  姓名
                </label>
                <input
                  type="text"
                  id="name"
                  className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary"
                />
              </div>
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                  邮箱
                </label>
                <input
                  type="email"
                  id="email"
                  className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary"
                />
              </div>
              <button
                type="submit"
                className="w-full bg-primary text-white py-2 px-4 rounded-md hover:bg-blue-600 transition-colors"
              >
                发送消息
              </button>
            </form>
          </div>
        </section>
      </div>
    </main>
  )
} 