/*
 * @Author: mckay
 * @Date: 2019-11-29 13:54:12
 * @LastEditors: mckay
 * @LastEditTime: 2019-11-29 17:17:22
 * @Description: ''
 */
import {
	// action,
	Module,
	mutation,
	VuexModule
} from 'vuex-class-component';

/**
 * MenuStore define
 *
 * @export
 * @class MenuStore
 * @extends {VuexModule}
 */
@Module({ namespacedPath: 'menu/' })
export class MenuStore extends VuexModule {
	private MenuData: any[] = [];

	/**
	 * set menu
	 *
	 * @param {*} MenuData
	 * @memberof MenuStore
	 */
	@mutation
	public setMenu(MenuData: any): void {
		this.MenuData = MenuData;
	}

	/**
	 * 获取menu
	 *
	 * @readonly
	 * @type {*}
	 * @memberof MenuStore
	 */
	public get menuData(): any {
		return this.MenuData;
	}
}

export const menu: any = MenuStore.ExtractVuexModule(MenuStore);
