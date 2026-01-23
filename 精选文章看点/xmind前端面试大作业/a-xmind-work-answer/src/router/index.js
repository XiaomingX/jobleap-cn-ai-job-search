import Vue from 'vue'

import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: '/',
  routes: [
    {
      path: '/',
      redirect: '/pocketBook'
    },
    {
      path: '/pocketBook',
      name: "pocketBook",
      component: () => import("@/pages/pocketBook"),
      meta: {
        title: 'work'
      }
    }
  ],
  scrollBehavior: () => ({y: 0})
});