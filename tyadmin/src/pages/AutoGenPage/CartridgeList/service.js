import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCartridge(params) {
  return request('/api/xadmin/v1/cartridge', {
    params,
  });
}
export async function removeCartridge(params) {
  return request(`/api/xadmin/v1/cartridge/${params}`, {
    method: 'DELETE',
  });
}
export async function addCartridge(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/cartridge', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCartridge(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/cartridge/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCartridgeVerboseName(params) {
  return request('/api/xadmin/v1/cartridge/verbose_name', {
    params,
  });
}
export async function queryCartridgeListDisplay(params) {
  return request('/api/xadmin/v1/cartridge/list_display', {
    params,
  });
}
export async function queryCartridgeDisplayOrder(params) {
  return request('/api/xadmin/v1/cartridge/display_order', {
    params,
  });
}


