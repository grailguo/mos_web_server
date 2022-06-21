import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryQuantMethodCodeCounter(params) {
  return request('/api/xadmin/v1/quant_method_code_counter', {
    params,
  });
}
export async function removeQuantMethodCodeCounter(params) {
  return request(`/api/xadmin/v1/quant_method_code_counter/${params}`, {
    method: 'DELETE',
  });
}
export async function addQuantMethodCodeCounter(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/quant_method_code_counter', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateQuantMethodCodeCounter(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/quant_method_code_counter/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryQuantMethodCodeCounterVerboseName(params) {
  return request('/api/xadmin/v1/quant_method_code_counter/verbose_name', {
    params,
  });
}
export async function queryQuantMethodCodeCounterListDisplay(params) {
  return request('/api/xadmin/v1/quant_method_code_counter/list_display', {
    params,
  });
}
export async function queryQuantMethodCodeCounterDisplayOrder(params) {
  return request('/api/xadmin/v1/quant_method_code_counter/display_order', {
    params,
  });
}


