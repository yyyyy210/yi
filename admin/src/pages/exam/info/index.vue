<!--
 * @Author: mckay
 * @Date: 2019-12-13 17:36:35
 * @LastEditors: mckay
 * @LastEditTime: 2019-12-13 18:02:42
 * @Description: 
 -->
<template>
    <div>
        <span>fsdfsdfsdfs</span>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator';
import { BaseView } from '~/core/views/ViewBase';
import IMenu from '~/models/ModelMenu';

@Component({})
export default class ExamInfo extends BaseView {
	constructor() {
		super();
    }
    
	/** 自定义SEO头部数据 */
	public head(): any {
		return {
            title: '考试信息'
        }
    }

	/** 菜单 */
	private menuData: Array<IMenu> = [
		{
			name: '考试信息',
			title: '考试信息',
			path: ''
		}
	];
    
	public created(): void {
		// this.$vxm.menu.setMenu(this.menuData);
	}
}
</script>