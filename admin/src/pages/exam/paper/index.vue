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
				<Button type="primary" @click="setPaper">添加试卷</Button>
			</div>
			<Table :columns="columns1" :data="sourceData">
				<template slot-scope="{ row, index }" slot="action">
					<Button type="primary" size="small" style="margin-right: 5px" @click="patchPaper(row)">编辑</Button>
					<Button type="error" size="small" @click="delPaper(row._id.$oid)">删除</Button>
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
export default class Paper extends BaseView {
	private data() {
		return {
			columns1: [
                { title: '名称', key: 'name' },
                { title: '课程', key: 'courseId' },
				{ title: '试卷方式', key: 'type' },// 选题，随机
				{ title: '试卷时长类型', key: 'timeType' },// 根据题，根据试卷
				{ title: '试卷时长', key: 'timeAll' },// 根据试卷时长
                { title: '试题', key: 'text' },// 问题ID:排序:时长|问题ID:排序:时长
                { title: '操作', slot: 'action', width: 150, align: 'center' }
			]
		};
    }

	/** 原始数据 */
	private sourceData: any;
    
	/** 初始化前将页面数据提取 */
	public async asyncData({ params, app, req }: any): Promise<any> {
		const res = await localService.getPaper()
		return { sourceData: res.data.data };
	}

	/** 下拉刷新 */
	private async onRefresh(): Promise<any> {
		const res: any = await localService.getPaper();
		this.sourceData = res.data.data;
	}

	public async setPaper() {
		const res = await localService.setPaper({
			'name': '试卷一',
			'courseId': 2,
			'type': 1,
			'timeType': 2,
			'timeAll': 120,
            'text': '11:1:1'
		});
		this.sourceData.push(res.data.data);
	}

	public async delPaper(id: string) {
		const res = await localService.delPaper(id);
		this.onRefresh();
	}

	public async patchPaper(data: any) {
		const res = await localService.patchPaper(data._id.$oid, {
			"name": "试卷二",
			"text": "11:1:2"
		});
		this.onRefresh();
	}
}
</script>