// @ts-nocheck
import { Plugin } from 'D:/workspace/data_platform/github/mos_web_server/tyadmin/node_modules/@umijs/runtime';

const plugin = new Plugin({
  validKeys: ['modifyClientRenderOpts','patchRoutes','rootContainer','render','onRouteChange','dva','getInitialState','locale','locale','request',],
});
plugin.register({
  apply: require('D:/workspace/data_platform/github/mos_web_server/tyadmin/node_modules/umi-plugin-antd-icon-config/lib/app.js'),
  path: 'D:/workspace/data_platform/github/mos_web_server/tyadmin/node_modules/umi-plugin-antd-icon-config/lib/app.js',
});
plugin.register({
  apply: require('D:/workspace/data_platform/github/mos_web_server/tyadmin/src/.umi/plugin-dva/runtime.tsx'),
  path: 'D:/workspace/data_platform/github/mos_web_server/tyadmin/src/.umi/plugin-dva/runtime.tsx',
});
plugin.register({
  apply: require('../plugin-initial-state/runtime'),
  path: '../plugin-initial-state/runtime',
});
plugin.register({
  apply: require('D:/workspace/data_platform/github/mos_web_server/tyadmin/src/.umi/plugin-locale/runtime.tsx'),
  path: 'D:/workspace/data_platform/github/mos_web_server/tyadmin/src/.umi/plugin-locale/runtime.tsx',
});
plugin.register({
  apply: require('../plugin-model/runtime'),
  path: '../plugin-model/runtime',
});

export { plugin };
