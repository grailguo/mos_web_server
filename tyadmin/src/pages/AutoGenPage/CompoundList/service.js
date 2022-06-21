import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCompound(params) {
  return request('/api/xadmin/v1/compound', {
    params,
  });
}
export async function removeCompound(params) {
  return request(`/api/xadmin/v1/compound/${params}`, {
    method: 'DELETE',
  });
}
export async function addCompound(params) {
  let fileFieldList = ["structural_formula","safety_data_sheet"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/compound', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCompound(params, id) {
  let fileFieldList = ["structural_formula","safety_data_sheet"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/compound/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCompoundVerboseName(params) {
  return request('/api/xadmin/v1/compound/verbose_name', {
    params,
  });
}
export async function queryCompoundListDisplay(params) {
  return request('/api/xadmin/v1/compound/list_display', {
    params,
  });
}
export async function queryCompoundDisplayOrder(params) {
  return request('/api/xadmin/v1/compound/display_order', {
    params,
  });
}


