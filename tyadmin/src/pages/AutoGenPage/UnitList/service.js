import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryUnit(params) {
  return request('/api/xadmin/v1/unit', {
    params,
  });
}
export async function removeUnit(params) {
  return request(`/api/xadmin/v1/unit/${params}`, {
    method: 'DELETE',
  });
}
export async function addUnit(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/unit', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateUnit(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/unit/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryUnitVerboseName(params) {
  return request('/api/xadmin/v1/unit/verbose_name', {
    params,
  });
}
export async function queryUnitListDisplay(params) {
  return request('/api/xadmin/v1/unit/list_display', {
    params,
  });
}
export async function queryUnitDisplayOrder(params) {
  return request('/api/xadmin/v1/unit/display_order', {
    params,
  });
}


