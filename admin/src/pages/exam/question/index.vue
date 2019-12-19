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
				<Button type="primary" @click="setQuestion">添加试题</Button>
			</div>
			<Table :columns="columns1" :data="sourceData">
				<template slot-scope="{ row, index }" slot="action">
					<Button type="primary" size="small" style="margin-right: 5px" @click="patchQuestion(row)">编辑</Button>
					<Button type="error" size="small" @click="delQuestion(row._id.$oid)">删除</Button>
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
export default class Question extends BaseView {
	private data() {
		return {
			columns1: [
                { title: '课程', key: 'courseId' },
                { title: '试题类型', key: 'typeId' },
				{ title: '难度', key: 'grade' },
				{ title: '题目', key: 'subject' },
				{ title: '答案', key: 'answer' },
                { title: '标签', key: 'tag' },
                { title: '解析', key: 'text' },
                { title: '操作', slot: 'action', width: 150, align: 'center' }
			]
		};
    }

	/** 原始数据 */
	private sourceData: any;
    
	/** 初始化前将页面数据提取 */
	public async asyncData({ params, app, req }: any): Promise<any> {
		const res = await localService.getQuestion()
		return { sourceData: res.data.data };
	}

	/** 下拉刷新 */
	private async onRefresh(): Promise<any> {
		const res: any = await localService.getQuestion();
		this.sourceData = res.data.data;
	}

	public async setQuestion() {
		const res = await localService.setQuestion({
			'courseId': 11,
			'typeId': 2,
			'grade': 1,
			'subject': '题目一',
			'answer': '答案一',
            'tag': '关键词',
            'text': '解析一',
		});
		this.sourceData.push(res.data.data);
	}

	public async delQuestion(id: string) {
		const res = await localService.delQuestion(id);
		this.onRefresh();
	}

	public async patchQuestion(data: any) {
		const res = await localService.patchQuestion(data._id.$oid, {
			"subject": "题目二",
			"text": "解析备注二"
		});
		this.onRefresh();
	}
}
</script>