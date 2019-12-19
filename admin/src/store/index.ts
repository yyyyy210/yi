/*
 * @Author: mckay
 * @Date: 2019-11-26 17:01:49
 * @LastEditors: mckay
 * @LastEditTime: 2019-12-13 17:34:41
 * @Description: ''
 */
import Vue from 'vue';
import Vuex from 'vuex';
import { root, RootStore } from './modules/root';
import { menu, MenuStore } from './modules/menu';

Vue.use(Vuex);

/** store */
export const store: any = new Vuex.Store({
	modules: {
		root,
		menu
	}
});

/** 注册store实例 */
Vue.prototype.$vxm = {
	root: RootStore.CreateProxy(store, RootStore),
	// menu: CartsStore.CreateProxy(store, MenuStore)
};

/** 定义接口格式用于TS语法提示 */
declare module 'vue/types/vue' {

	/** define vue interface */
	// tslint:disable-next-line:interface-name
	interface Vue {
		$vxm: {
			root: RootStore;
			menu: MenuStore;
		};
	}
}
