var path = require('path')

module.exports = {
  entry: './frontend/index.js',
  output: {
    path: __dirname + '/git_ext/static',
    filename: 'index.js',
    libraryTarget: 'amd'
  },
  module: {
    loaders: [{
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      loader: 'babel-loader',
      query: {
        presets: ['env']
      }
    }, {
      test: /\.vue$/,
      loader: 'vue-loader',
      options: {
        options: {
          postcss: {
            plugins: [require('autoprefixer')],
            options: {
              parser: require('sugarss')
            }
          }
        }
      }
    }]
  },
  devtool: (process.env.NODE_ENV === 'develop') ? 'inline-source-map' : '',
  resolve: {
    extensions: ['.js'],
    alias: {
      vue: 'vue/dist/vue.common.js',
      animate: path.resolve('./node_modules/animate-sass')
    }
  },
  externals: [
    'base/js/namespace'
  ]
}
