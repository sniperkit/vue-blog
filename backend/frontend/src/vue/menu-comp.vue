<template>
	<div>
      <a id="menuLink" class="menu-link animated fadeIn" @click="menuon">
          <span></span>
      </a>
      <transition name="menu-slide">
          <div id="menu" v-show="show">
              <ul class="pure-menu-list">
                  <li class="pure-menu-item">
                      <a href="#" class="pure-menu-link"><i id="icon-menu" class="iconfont icon-icontitlehuishouye"></i>Home</a>
                  </li>

                  <li class="pure-menu-item">
                      <a href="/manage/" class="pure-menu-link"><i id="icon-menu" class="iconfont icon-manage"></i>Manage</a>
                  </li>

                  <li class="pure-menu-item">
                      <a href="#/tag" class="pure-menu-link"><i id="icon-menu" class="iconfont icon-tag"></i>Tags</a>
                  </li>

                  <li class="pure-menu-item">
                      <a href="#/about" class="pure-menu-link"><i id="icon-menu" class="iconfont icon-about"></i>About</a>
                  </li>
              </ul>
              <i @click="menuoff" class="iconfont icon-left"></i>
          </div>
      </transition>

      <div class="pure-menu pure-menu-horizontal" style="text-align: center;padding: 30px">
        <ul class="pure-menu-list" id="top-menu">
            <li class="pure-menu-item"><a href="/#/" id="top-menu-font">Hello</a></li>
            <li class="pure-menu-item"><a href="#/tag" id="top-menu-font">Tags</a></li>
            <li class="pure-menu-item"><a href="#/archives" id="top-menu-font">Archives</a></li>
            <li @click="manageLogin" class="pure-menu-item"><a id="top-menu-font">Manage</a></li>
            <li class="pure-menu-item"><a href="#/about" id="top-menu-font">About</a></li>
        </ul>

    </div>

      <!-- <div id="background-image" class="header animated fadeIn" :style="{'background-image': 'url(' + img_url +')'}">
        <h1 class="">{{header}}</h1>
        <div v-show="loadShow" style="margin-top: -50px" class="ui active centered inline loader"></div>
        <button @click="changeImg" title="点击切换图片" class="pure-button click-btn">click!</button>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      show: false,
      img_url: '/static/image/head1.jpeg/',
      loadShow:true
    }
  },
  props:['header'],
  methods:{
    menuon:function() {
        this.show = true;
        this.$emit('menuon')
    },
    menuoff:function() {
        this.show = false;
        this.$emit('menuoff')
    },
    // changeImg:function() {
    //   var self = this;
    //   axios.get('127.0.0.1:8000/api/change_img/').then(function(response){
    //     self.img_url = response.data.img_url;
    //     self.loadShow = false
    //   })
    // },
    manageLogin:function() {
      axios.get('/api/request_user/', {
        headers:{ 'Authorization': 'Token ' + Cookies.get('token') }
      }).then(function(response){
        window.location.href = "/manage/"
      })
      .catch(function(){
        window.location.href = "/#/login/"
      })
    }
  }
}
</script>
