const gulp = require('gulp')
const webpack = require('webpack-stream')

const dist = '../web'

gulp.task('build-js', () => {
  return gulp
    .src('./src/index.js')
    .pipe(
      webpack({
        mode: 'development',
        output: {
          filename: 'main.js',
        },
        watch: false,
        devtool: 'source-map',
        module: {
          rules: [
            {
              test: /\.m?js$/,
              exclude: /(node_modules|bower_components)/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: [
                    [
                      '@babel/preset-env',
                      {
                        debug: true,
                        corejs: 3,
                        useBuiltIns: 'usage',
                      },
                    ],
                  ],
                },
              },
            },
          ],
        },
      })
    )
    .pipe(gulp.dest(dist))
})

gulp.task('watch', () => {
  gulp.watch('./src/**/*.js', gulp.parallel('build-js'))
})

gulp.task('build', gulp.parallel('build-js'))

gulp.task('prod', () => {
  return gulp
    .src('./src/index.js')
    .pipe(
      webpack({
        mode: 'production',
        output: {
          filename: 'main.js',
        },
        module: {
          rules: [
            {
              test: /\.m?js$/,
              exclude: /(node_modules|bower_components)/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: [
                    [
                      '@babel/preset-env',
                      {
                        corejs: 3,
                        useBuiltIns: 'usage',
                      },
                    ],
                  ],
                },
              },
            },
          ],
        },
      })
    )
    .pipe(gulp.dest(dist))
})

gulp.task('default', gulp.parallel('watch', 'build'))
