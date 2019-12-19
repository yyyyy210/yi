<!--
 * @Author: mckay
 * @Date: 2019-12-16 17:18:11
 * @LastEditors  : mckay
 * @LastEditTime : 2019-12-18 11:42:47
 * @Description: 
 -->
<template>
	<div>
		<!-- <PageHead /> -->
		<div style="margin: 10px; padding: 30px; background: #fff; border-radius: 4px;">
			<div style="margin-bottom: 15px">
				<Button type="primary" @click="setCourse">添加课程</Button>
			</div>
			<Table :columns="columns1" :data="sourceData">
				<template slot-scope="{ row, index }" slot="action">
					<Button type="primary" size="small" style="margin-right: 5px" @click="patchCourse(row)">编辑</Button>
					<Button type="error" size="small" @click="delCourse(row._id.$oid)">删除</Button>
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
export default class Course extends BaseView {
	private data() {
		return {
			columns1: [
				{ title: '名称', key: 'name' },
                { title: '分类', key: 'CourseCategoryId' },
                { title: '封面', key: 'img' },
                { title: '时间范围', key: 'timeArea' },
				{ title: '需要购买', key: 'isBuy' },
                { title: '积分', key: 'score' },
				{ title: '状态', key: 'state' },
				{ title: '备注', key: 'text' },
                { title: '操作', slot: 'action', width: 150, align: 'center' }

			]
		};
    }

	/** 原始数据 */
	private sourceData: any;
    
	/** 初始化前将页面数据提取 */
	public async asyncData({ params, app, req }: any): Promise<any> {
		const res = await localService.getCourse()
		return { sourceData: res.data.data };
	}

	/** 下拉刷新 */
	private async onRefresh(): Promise<any> {
		const res: any = await localService.getCourse();
		this.sourceData = res.data.data;
	}

	public async setCourse() {
		const res = await localService.setCourse({
			'name': '课程一',
			'CourseCategoryId': '10',
			'img': '111.jpg',
			'timeArea': '2019:11:11',
			'isBuy': true,
			'score': '7',
			'state': true,
			'text': '这是个备注'
		});
		this.sourceData.push(res.data.data);
	}

	public async delCourse(id: string) {
		const res = await localService.delCourse(id);
		this.onRefresh();
	}

	public async patchCourse(data: any) {
		const res = await localService.patchCourse(data._id.$oid, {
			"name": "课程二",
			"text": "这是个备注二"
		});
		this.onRefresh();
	}
}
</script>