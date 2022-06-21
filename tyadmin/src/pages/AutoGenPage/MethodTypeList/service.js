import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryMethodType(params) {
  return request('/api/xadmin/v1/method_type', {
    params,
  });
}
export async function removeMethodType(params) {
  return request(`/api/xadmin/v1/method_type/${params}`, {
    method: 'DELETE',
  });
}
export async function addMethodType(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/method_type', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateMethodType(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/method_type/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryMethodTypeVerboseName(params) {
  return request('/api/xadmin/v1/method_type/verbose_name', {
    params,
  });
}
export async function queryMethodTypeListDisplay(params) {
  return request('/api/xadmin/v1/method_type/list_display', {
    params,
  });
}
export async function queryMethodTypeDisplayOrder(params) {
  return request('/api/xadmin/v1/method_type/display_order', {
    params,
  });
}


