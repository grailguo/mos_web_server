import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function querySpectrum(params) {
  return request('/api/xadmin/v1/spectrum', {
    params,
  });
}
export async function removeSpectrum(params) {
  return request(`/api/xadmin/v1/spectrum/${params}`, {
    method: 'DELETE',
  });
}
export async function addSpectrum(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/spectrum', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateSpectrum(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/spectrum/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function querySpectrumVerboseName(params) {
  return request('/api/xadmin/v1/spectrum/verbose_name', {
    params,
  });
}
export async function querySpectrumListDisplay(params) {
  return request('/api/xadmin/v1/spectrum/list_display', {
    params,
  });
}
export async function querySpectrumDisplayOrder(params) {
  return request('/api/xadmin/v1/spectrum/display_order', {
    params,
  });
}


