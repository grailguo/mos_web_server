import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCompoundCodeCounter(params) {
  return request('/api/xadmin/v1/compound_code_counter', {
    params,
  });
}
export async function removeCompoundCodeCounter(params) {
  return request(`/api/xadmin/v1/compound_code_counter/${params}`, {
    method: 'DELETE',
  });
}
export async function addCompoundCodeCounter(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/compound_code_counter', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCompoundCodeCounter(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/compound_code_counter/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCompoundCodeCounterVerboseName(params) {
  return request('/api/xadmin/v1/compound_code_counter/verbose_name', {
    params,
  });
}
export async function queryCompoundCodeCounterListDisplay(params) {
  return request('/api/xadmin/v1/compound_code_counter/list_display', {
    params,
  });
}
export async function queryCompoundCodeCounterDisplayOrder(params) {
  return request('/api/xadmin/v1/compound_code_counter/display_order', {
    params,
  });
}


