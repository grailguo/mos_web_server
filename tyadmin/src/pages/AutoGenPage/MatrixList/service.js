import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryMatrix(params) {
  return request('/api/xadmin/v1/matrix', {
    params,
  });
}
export async function removeMatrix(params) {
  return request(`/api/xadmin/v1/matrix/${params}`, {
    method: 'DELETE',
  });
}
export async function addMatrix(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/matrix', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateMatrix(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/matrix/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryMatrixVerboseName(params) {
  return request('/api/xadmin/v1/matrix/verbose_name', {
    params,
  });
}
export async function queryMatrixListDisplay(params) {
  return request('/api/xadmin/v1/matrix/list_display', {
    params,
  });
}
export async function queryMatrixDisplayOrder(params) {
  return request('/api/xadmin/v1/matrix/display_order', {
    params,
  });
}


