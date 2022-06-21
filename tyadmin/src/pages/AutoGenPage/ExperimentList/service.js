import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryExperiment(params) {
  return request('/api/xadmin/v1/experiment', {
    params,
  });
}
export async function removeExperiment(params) {
  return request(`/api/xadmin/v1/experiment/${params}`, {
    method: 'DELETE',
  });
}
export async function addExperiment(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/experiment', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateExperiment(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/experiment/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryExperimentVerboseName(params) {
  return request('/api/xadmin/v1/experiment/verbose_name', {
    params,
  });
}
export async function queryExperimentListDisplay(params) {
  return request('/api/xadmin/v1/experiment/list_display', {
    params,
  });
}
export async function queryExperimentDisplayOrder(params) {
  return request('/api/xadmin/v1/experiment/display_order', {
    params,
  });
}


