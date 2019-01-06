'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  // API_HOST:'"http://172.18.214.121:80"'
  API_HOST:'"http://192.168.1.11:80"'
})
