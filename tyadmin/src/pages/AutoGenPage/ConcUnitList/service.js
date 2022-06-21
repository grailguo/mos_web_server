import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryConcUnit(params) {
  return request('/api/xadmin/v1/conc_unit', {
    params,
  });
}
export async function removeConcUnit(params) {
  return request(`/api/xadmin/v1/conc_unit/${params}`, {
    method: 'DELETE',
  });
}
export async function addConcUnit(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/conc_unit', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateConcUnit(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/conc_unit/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryConcUnitVerboseName(params) {
  return request('/api/xadmin/v1/conc_unit/verbose_name', {
    params,
  });
}
export async function queryConcUnitListDisplay(params) {
  return request('/api/xadmin/v1/conc_unit/list_display', {
    params,
  });
}
export async function queryConcUnitDisplayOrder(params) {
  return request('/api/xadmin/v1/conc_unit/display_order', {
    params,
  });
}


