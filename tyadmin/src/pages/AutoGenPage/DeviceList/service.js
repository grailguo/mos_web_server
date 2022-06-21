import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryDevice(params) {
  return request('/api/xadmin/v1/device', {
    params,
  });
}
export async function removeDevice(params) {
  return request(`/api/xadmin/v1/device/${params}`, {
    method: 'DELETE',
  });
}
export async function addDevice(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/device', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateDevice(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/device/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryDeviceVerboseName(params) {
  return request('/api/xadmin/v1/device/verbose_name', {
    params,
  });
}
export async function queryDeviceListDisplay(params) {
  return request('/api/xadmin/v1/device/list_display', {
    params,
  });
}
export async function queryDeviceDisplayOrder(params) {
  return request('/api/xadmin/v1/device/display_order', {
    params,
  });
}


