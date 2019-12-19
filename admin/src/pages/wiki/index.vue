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
				<Button type="primary" @click="setWiki">添加Wiki</Button>
			</div>
            {{content}}
			<Table :columns="columns1" :data="sourceData">
				<template slot-scope="{ row, index }" slot="action">
					<Button type="primary" size="small" style="margin-right: 5px" @click="patchWiki(row)">编辑</Button>
					<Button type="error" size="small" @click="delWiki(row._id.$oid)">删除</Button>
				</template>
			</Table>
		</div>
        <div>
            <no-ssr>
                <vue-editor v-model="content"></vue-editor>
            </no-ssr>
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
export default class Wiki extends BaseView {
	private data() {
		return {
            content: '<h1>Some initial content</h1>',
			columns1: [
                { title: '名称', key: 'name' },
                { title: '分类', key: 'CourseCategoryId' },
				{ title: '类型', key: 'type' },
				{ title: '标签', key: 'tag' },
				{ title: '来自', key: 'source' },
				{ title: '内容', key: 'text' },
                { title: '操作', slot: 'action', width: 150, align: 'center' }
			]
		};
    }

	/** 原始数据 */
	private sourceData: any;
    
	/** 初始化前将页面数据提取 */
	public async asyncData({ params, app, req }: any): Promise<any> {
		const res = await localService.getWiki()
		return { sourceData: res.data.data };
	}

	/** 下拉刷新 */
	private async onRefresh(): Promise<any> {
		const res: any = await localService.getWiki();
		this.sourceData = res.data.data;
	}

	public async setWiki() {
		const res = await localService.setWiki({
			'name': '文档一',
			'CourseCategoryId': '11',
			'type': '1',
			'tag': '关键词',
			'source': 'http://www.baidu.com',
			'text': '文档备注',
		});
		this.sourceData.push(res.data.data);
	}

	public async delWiki(id: string) {
		const res = await localService.delWiki(id);
		this.onRefresh();
	}

	public async patchWiki(data: any) {
		const res = await localService.patchWiki(data._id.$oid, {
			"name": "文档二",
			"text": "文档备注二"
		});
		this.onRefresh();
	}
}
</script>