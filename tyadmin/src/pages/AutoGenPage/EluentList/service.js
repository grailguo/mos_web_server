import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryEluent(params) {
  return request('/api/xadmin/v1/eluent', {
    params,
  });
}
export async function removeEluent(params) {
  return request(`/api/xadmin/v1/eluent/${params}`, {
    method: 'DELETE',
  });
}
export async function addEluent(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/eluent', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateEluent(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/eluent/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryEluentVerboseName(params) {
  return request('/api/xadmin/v1/eluent/verbose_name', {
    params,
  });
}
export async function queryEluentListDisplay(params) {
  return request('/api/xadmin/v1/eluent/list_display', {
    params,
  });
}
export async function queryEluentDisplayOrder(params) {
  return request('/api/xadmin/v1/eluent/display_order', {
    params,
  });
}


