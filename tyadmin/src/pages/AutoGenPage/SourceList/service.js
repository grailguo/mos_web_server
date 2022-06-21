import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function querySource(params) {
  return request('/api/xadmin/v1/source', {
    params,
  });
}
export async function removeSource(params) {
  return request(`/api/xadmin/v1/source/${params}`, {
    method: 'DELETE',
  });
}
export async function addSource(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/source', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateSource(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/source/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function querySourceVerboseName(params) {
  return request('/api/xadmin/v1/source/verbose_name', {
    params,
  });
}
export async function querySourceListDisplay(params) {
  return request('/api/xadmin/v1/source/list_display', {
    params,
  });
}
export async function querySourceDisplayOrder(params) {
  return request('/api/xadmin/v1/source/display_order', {
    params,
  });
}


