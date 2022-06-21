import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryQuantMethod(params) {
  return request('/api/xadmin/v1/quant_method', {
    params,
  });
}
export async function removeQuantMethod(params) {
  return request(`/api/xadmin/v1/quant_method/${params}`, {
    method: 'DELETE',
  });
}
export async function addQuantMethod(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/quant_method', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateQuantMethod(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/quant_method/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryQuantMethodVerboseName(params) {
  return request('/api/xadmin/v1/quant_method/verbose_name', {
    params,
  });
}
export async function queryQuantMethodListDisplay(params) {
  return request('/api/xadmin/v1/quant_method/list_display', {
    params,
  });
}
export async function queryQuantMethodDisplayOrder(params) {
  return request('/api/xadmin/v1/quant_method/display_order', {
    params,
  });
}


