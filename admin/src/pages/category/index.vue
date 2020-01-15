<!--
 * @Author: mckay
 * @Date: 2019-12-16 17:18:11
 * @LastEditors  : mckay
 * @LastEditTime : 2019-12-24 19:33:17
 * @Description: 
 -->
<template>
	<div>
		<!-- <PageHead /> -->
		<div style="margin: 10px; padding: 30px; background: #fff; border-radius: 4px;">
			<div style="margin-bottom: 15px">
				<Button type="primary" @click="setCategory">添加分类</Button>
			</div>
			<Table :columns="columns1" :data="sourceData">
				<template slot-scope="{ row, index }" slot="action">
					<Button type="primary" size="small" style="margin-right: 5px" @click="patchCategory(row)">编辑</Button>
					<Button type="error" size="small" @click="delCategory(row._id.$oid)">删除</Button>
				</template>
			</Table>
		</div>
	</div>
</template>
<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator';
import { BaseView } from '~/core/views/ViewBase';
import localService from '~/service/ServiceLocal';
// import PageHead from "~/components/PageHead.vue"

@Component({
	components: {
		// PageHead
	}
})
export default class Category extends BaseView {
	private data() {
		return {
			columns1: [
				{ title: '名称', key: 'name' },
				{ title: '父类', key: 'parentId' },
				{ title: '备注', key: 'text' },
                { title: '操作', slot: 'action', width: 150, align: 'center' }

			]
		};
    }

	/** 原始数据 */
	private sourceData: any;
    
	/** 初始化前将页面数据提取 */
	public async asyncData({ params, app, req }: any): Promise<any> {
		const res = await localService.getCategory()
		return { sourceData: res.data.data };
	}

	/** 下拉刷新 */
	private async onRefresh(): Promise<any> {
		const res: any = await localService.getCategory();
		this.sourceData = res.data.data;
	}

	public async setCategory() {
		const res = await localService.setCategory({
			'name': '分类一',
			'parentId': '10',
			'text': '这是个备注'
		});
		this.sourceData.push(res.data.data);
	}

	public async delCategory(id: string) {
		const res = await localService.delCategory(id);
		this.onRefresh();
	}

	public async patchCategory(data: any) {
		const res = await localService.patchCategory(data._id.$oid, {
			"name": "分类二",
			"text": "这是个备注二"
		});
		this.onRefresh();
	}
}
</script>