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
				<Button type="primary" @click="setUser">添加用户</Button>
			</div>
			<Table :columns="columns1" :data="sourceData">
				<template slot-scope="{ row, index }" slot="action">
					<Button type="primary" size="small" style="margin-right: 5px" @click="patchUser(row)">编辑</Button>
					<Button type="error" size="small" @click="delUser(row._id.$oid)">删除</Button>
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
export default class User extends BaseView {
	private data() {
		return {
			columns1: [
				{ title: '名称', key: 'name' },
				{ title: '邮箱', key: 'email' },
				{ title: '电话', key: 'phone' },
				{ title: '备注', key: 'text' },
				{ title: '微信信息', key: 'wx' },
				{ title: '积分', key: 'score' },
				{ title: '课程', key: 'courses' },
				{ title: '操作', slot: 'action', width: 150, align: 'center' }
			]
		};
    }

	/** 原始数据 */
	private sourceData: any;
    
	/** 初始化前将页面数据提取 */
	public async asyncData({ params, app, req }: any): Promise<any> {
		const res = await localService.getUser()
		return { sourceData: res.data.data };
	}

	/** 下拉刷新 */
	private async onRefresh(): Promise<any> {
		const res: any = await localService.getUser();
		this.sourceData = res.data.data;
	}

	public async setUser() {
		const res = await localService.setUser({
			'name': '用户一',
			'email': '321@qq.com',
			'phone': '131111111111',
			'text': '用户描述',
			'wx': '{"name": "mm", "openId":"sdfsdfgs86735342"}',
			'score': '7',
			'courses': '1,2,3,4,5',
		});
		this.sourceData.push(res.data.data);
	}

	public async delUser(id: string) {
		const res = await localService.delUser(id);
		this.onRefresh();
	}

	public async patchUser(data: any) {
		const res = await localService.patchUser(data._id.$oid, {
			"name": "用户二",
			"text": "用户备注二"
		});
		this.onRefresh();
	}
}
</script>