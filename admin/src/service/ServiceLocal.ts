import { BaseService, BaseOption } from '~/core/service/ServiceBase';
import configService from '~/core/service/ServiceConfig';

/**
 * 本地 node服务
 *
 * @class LocalService
 * @extends {BaseService}
 */
class LocalService extends BaseService {
	constructor() {
		const baseOption: BaseOption = new BaseOption();
		baseOption.baseUrl = configService.getConfig().localUrl;
		baseOption.isLocalHost = false; // 不是本地调用
		super(baseOption);
	}

	/**
	 * 课程
	 *
	 * @returns {Promise<any>}
	 * @memberof LocalService
	 */
	public async getCourse(): Promise<any> {
		return await this.get('api/course');
	}

	/* 
	 */

	public async setCourse(data: any): Promise<any> {
		return await this.post('api/course', data)
	}

	/* 
	 */
	public async delCourse(id: string): Promise<any> {
		return await this.delete(`api/course/${id}`)
	}

	/* 
	 */
	public async patchCourse(id: string, data: any): Promise<any> {
		return await this.patch(`api/course/${id}`, data)
	}

	/**
	 * 分类
	 *
	 * @returns {Promise<any>}
	 * @memberof LocalService
	 */
	public async getCategory(): Promise<any> {
		return await this.get('api/category');
	}

	/* 
	 */

	public async setCategory(data: any): Promise<any> {
		return await this.post('api/category', data)
	}

	/* 
	 */
	public async delCategory(id: string): Promise<any> {
		return await this.delete(`api/category/${id}`)
	}

	/* 
	 */
	public async patchCategory(id: string, data: any): Promise<any> {
		return await this.patch(`api/category/${id}`, data)
	}

	/**
	 * 用户
	 *
	 * @returns {Promise<any>}
	 * @memberof LocalService
	 */
	public async getUser(): Promise<any> {
		return await this.get('api/user');
	}

	/* 
	 */

	public async setUser(data: any): Promise<any> {
		return await this.post('api/user', data)
	}

	/* 
	 */
	public async delUser(id: string): Promise<any> {
		return await this.delete(`api/user/${id}`)
	}

	/* 
	 */
	public async patchUser(id: string, data: any): Promise<any> {
		return await this.patch(`api/user/${id}`, data)
	}

	/**
	 * 文档
	 *
	 * @returns {Promise<any>}
	 * @memberof LocalService
	 */
	public async getWiki(): Promise<any> {
		return await this.get('api/wiki');
	}

	/* 
	 */

	public async setWiki(data: any): Promise<any> {
		return await this.post('api/wiki', data)
	}

	/* 
	 */
	public async delWiki(id: string): Promise<any> {
		return await this.delete(`api/wiki/${id}`)
	}

	/* 
	 */
	public async patchWiki(id: string, data: any): Promise<any> {
		return await this.patch(`api/wiki/${id}`, data)
	}

	/**
	 * 试题
	 *
	 * @returns {Promise<any>}
	 * @memberof LocalService
	 */
	public async getQuestion(): Promise<any> {
		return await this.get('api/question');
	}

	/* 
	 */

	public async setQuestion(data: any): Promise<any> {
		return await this.post('api/question', data)
	}

	/* 
	 */
	public async delQuestion(id: string): Promise<any> {
		return await this.delete(`api/question/${id}`)
	}

	/* 
	 */
	public async patchQuestion(id: string, data: any): Promise<any> {
		return await this.patch(`api/question/${id}`, data)
	}

	/**
	 * 试题
	 *
	 * @returns {Promise<any>}
	 * @memberof LocalService
	 */
	public async getPaper(): Promise<any> {
		return await this.get('api/paper');
	}

	/* 
	 */

	public async setPaper(data: any): Promise<any> {
		return await this.post('api/paper', data)
	}

	/* 
	 */
	public async delPaper(id: string): Promise<any> {
		return await this.delete(`api/paper/${id}`)
	}

	/* 
	 */
	public async patchPaper(id: string, data: any): Promise<any> {
		return await this.patch(`api/paper/${id}`, data)
	}
}

export default new LocalService();
