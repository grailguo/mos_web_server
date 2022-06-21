import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCompoundTag(params) {
  return request('/api/xadmin/v1/compound_tag', {
    params,
  });
}
export async function removeCompoundTag(params) {
  return request(`/api/xadmin/v1/compound_tag/${params}`, {
    method: 'DELETE',
  });
}
export async function addCompoundTag(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/compound_tag', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCompoundTag(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/compound_tag/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCompoundTagVerboseName(params) {
  return request('/api/xadmin/v1/compound_tag/verbose_name', {
    params,
  });
}
export async function queryCompoundTagListDisplay(params) {
  return request('/api/xadmin/v1/compound_tag/list_display', {
    params,
  });
}
export async function queryCompoundTagDisplayOrder(params) {
  return request('/api/xadmin/v1/compound_tag/display_order', {
    params,
  });
}


