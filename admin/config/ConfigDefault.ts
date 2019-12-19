/**
 * 基础配置
 *
 * @export
 * @class ConfigDefault
 */
export class ConfigDefault {

	/**
	 * content-type
	 */
	public static CONTENT_TYPE: string = 'content-type';

	/**
	 * Env dev of config default
	 */
	public static ENV_DEV: string = 'development';

	/**
	 * Env prod of config default
	 */
	public static ENV_PROD: string = 'production';

	/**
	 * 默认环境标识
	 * @description Env  of config default
	 */
	private _env: string = ConfigDefault.ENV_PROD;

	constructor() {
		// hole
	}

	/**
	 * 本地URL地址
	 *
	 * @type {string}
	 * @memberof ConfigDefault
	 */
	public localUrl: string = 'http://127.0.0.1';

	/**
	 * API统一前缀
	 */
	public getGlobalPrefix(): string {
		return 'api';
	}

	/**
	 * 获取当前环境标识
	 * @description Gets env
	 * @returns env
	 */
	public getEnv(): string {
		return this._env;
	}

	/**
	 * 更新环境标识
	 * @description Updates env
	 * @param env
	 */
	public updateEnv(env: string): void {
		this._env = env;
	}

	/**
	 * 鉴权白名单页面，在此列表内页面将进行登录判断
	 */
	public authWhiteList(): Array<string> {
		return [
			'/cart',
			'/goods',
			'/'
		];
	}
}
