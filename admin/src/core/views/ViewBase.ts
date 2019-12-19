/*
 * @Author: mckay
 * @Date: 2019-12-13 17:39:02
 * @LastEditors: mckay
 * @LastEditTime: 2019-12-13 17:55:20
 * @Description: 
 */
import { Vue } from 'nuxt-property-decorator';
import { IView } from '~/core/interfaces/IView';

/**
 * 基础视图类
 *
 * @export
 * @class BaseView
 * @extends {Vue}
 * @implements {IView}
 */
export class BaseView extends Vue implements IView {

	/**
	 * SEO Title
	 *
	 * @type {string}
	 * @memberof BaseView
	 */
	public title: string = '';

	/**
	 * SEO Description
	 *
	 * @type {string}
	 * @memberof BaseView
	 */
	public description: string = '';

	/**
	 * SEO Keywords
	 *
	 * @type {string}
	 * @memberof BaseView
	 */
	public keywords: string = '';

	public constructor() {
		super();
	}
}
