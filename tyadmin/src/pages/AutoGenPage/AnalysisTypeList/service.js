import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryAnalysisType(params) {
  return request('/api/xadmin/v1/analysis_type', {
    params,
  });
}
export async function removeAnalysisType(params) {
  return request(`/api/xadmin/v1/analysis_type/${params}`, {
    method: 'DELETE',
  });
}
export async function addAnalysisType(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/analysis_type', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateAnalysisType(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/analysis_type/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryAnalysisTypeVerboseName(params) {
  return request('/api/xadmin/v1/analysis_type/verbose_name', {
    params,
  });
}
export async function queryAnalysisTypeListDisplay(params) {
  return request('/api/xadmin/v1/analysis_type/list_display', {
    params,
  });
}
export async function queryAnalysisTypeDisplayOrder(params) {
  return request('/api/xadmin/v1/analysis_type/display_order', {
    params,
  });
}


