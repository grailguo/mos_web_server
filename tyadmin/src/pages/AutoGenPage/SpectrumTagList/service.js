import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function querySpectrumTag(params) {
  return request('/api/xadmin/v1/spectrum_tag', {
    params,
  });
}
export async function removeSpectrumTag(params) {
  return request(`/api/xadmin/v1/spectrum_tag/${params}`, {
    method: 'DELETE',
  });
}
export async function addSpectrumTag(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/spectrum_tag', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateSpectrumTag(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/spectrum_tag/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function querySpectrumTagVerboseName(params) {
  return request('/api/xadmin/v1/spectrum_tag/verbose_name', {
    params,
  });
}
export async function querySpectrumTagListDisplay(params) {
  return request('/api/xadmin/v1/spectrum_tag/list_display', {
    params,
  });
}
export async function querySpectrumTagDisplayOrder(params) {
  return request('/api/xadmin/v1/spectrum_tag/display_order', {
    params,
  });
}


