<!--
 * @Author: mckay
 * @Date: 2019-12-13 15:13:14
 * @LastEditors  : mckay
 * @LastEditTime : 2019-12-18 11:44:26
 * @Description: ''
 -->
<template>
    <Layout>
		<Sider hide-trigger width="256">
			<div class="logo"><img src="https://file.iviewui.com/admin-pro-dist/img/logo-dark.ab519d9f.png" /></div>
			<Menu theme="dark"  width="auto">
				<Submenu name="exam">
					<template slot="title">
						<Icon type="ios-navigate"></Icon>
						<span>考试管理</span>
					</template>
					<MenuItem name="info">考试信息</MenuItem>
					<MenuItem name="question">试题库</MenuItem>
					<MenuItem name="paper">试卷库</MenuItem>
				</Submenu>
				<MenuItem name="user">
					<Icon type="ios-contacts" />
					<span>用户信息</span>
				</MenuItem>
				<MenuItem name="category">
					<Icon type="ios-keypad" />
					<span>分类</span>
				</MenuItem>
				<MenuItem name="course">
					<Icon type="md-list-box" />
					<span>课程</span>
				</MenuItem>
				<MenuItem name="wiki">
					<Icon type="ios-school" />
					<span>知识库</span>
				</MenuItem>
				<MenuItem name="customprocess">
					<Icon type="md-qr-scanner" />
					<span>自定义任务</span>
				</MenuItem>
				<MenuItem name="pay">
					<Icon type="md-finger-print" />
					<span>支付</span>
				</MenuItem>
				<MenuItem name="setting">
					<Icon type="md-settings" />
					<span>设置</span>
				</MenuItem>
			</Menu>
		</Sider>
        <Layout>
            <Header style="padding: 0 15px">
				<Breadcrumb>
					<BreadcrumbItem to="/">Home</BreadcrumbItem>
					<BreadcrumbItem to="/">Components</BreadcrumbItem>
					<BreadcrumbItem>Breadcrumb</BreadcrumbItem>
				</Breadcrumb>
			</Header>
            <Content>
				<nuxt />
			</Content>
        </Layout>
    </Layout>
</template>
<style>

</style>
<style lang="stylus" scoped>
.logo {
    height: 63px;
    line-height: 63px;
    text-align: center;
    border-bottom: 1px solid #101117;
    background: #191a23;
	img {
		height: 80%;
		vertical-align: middle;
	}
}
.ivu-layout-header {
    background: #fff;
    padding: 0;
    box-shadow: 0 1px 4px rgba(0,21,41,.08);
    transition: all .2s ease-in-out;
}
.ivu-layout-sider {
	background: #191a23;
	min-height: 100vh;
}
.ivu-menu {
    display: block;
    margin: 0;
    padding: 0;
    outline: none;
    list-style: none;
    color: #515a6e;
    font-size: 14px;
    position: relative;
    z-index: 900;
}
.ivu-menu-dark {
    background: #191a23;
	&.ivu-menu-vertical{
		.ivu-menu-opened {
			background: #101117;
			.ivu-menu-submenu-title {
				background: #191a23;
			}
		}
	}
}
.ivu-layout-content {
    overflow: auto;
    height: 800px;
}
.ivu-menu-item, .ivu-menu-submenu {
	font-size: 15px;
}
</style>