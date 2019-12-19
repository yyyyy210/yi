export default {
	env: {},
	srcDir: './src/',
	head: {
		title: "mecbox",
		meta: [
			{ charset: "utf-8" },
			{ name: "viewport", content: "width=device-width, initial-scale=1" },
		],
		link: [
			{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }
		]
	},
	loading: { color: "#3B8070" },
	css: ['~/assets/css/App.styl'],
	build: {},
	buildModules: ["@nuxt/typescript-build"],
	modules: [
		"@nuxtjs/axios",
	],
	plugins: [
		{
			src: '~plugins/PluginIview',
			ssr: true
		},
		{
			src: '~/plugins/PluginAxios',
			ssr: true
		},
		{
			src: '~plugins/PluginEditor',
			ssr: false
		}
	],
	// axios: {
	// 	proxy: false,
	// 	retry: { retries: 3 },
	// 	credentials: true
	// },
}
