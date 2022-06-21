import { DeleteOutlined, DownOutlined, EditOutlined, PlusOutlined, ExportOutlined } from '@ant-design/icons';
import { notification, Button, Col, Descriptions, Divider, Dropdown, Form, Input, Menu, message, Popconfirm, Popover, Row, Select, Tag, Transfer, Switch } from 'antd';
import React, { useEffect, useRef, useState } from 'react';
import KeyOutlined from '@ant-design/icons/lib/icons/KeyOutlined';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable from 'mtianyan-pro-table';
import CreateForm from './components/CreateForm';
import { addSpectrum, querySpectrum, removeSpectrum, updateSpectrum, querySpectrumVerboseName, querySpectrumListDisplay, querySpectrumDisplayOrder} from './service';
import UpdateForm from './components/UpdateForm';
import UploadAvatar from '@/components/UploadAvatar';
import {queryExperiment, queryExperimentVerboseName} from '@/pages/AutoGenPage/ExperimentList/service';import {queryCompound, queryCompoundVerboseName} from '@/pages/AutoGenPage/CompoundList/service';import {queryMethodType, queryMethodTypeVerboseName} from '@/pages/AutoGenPage/MethodTypeList/service';import {querySpectrumTag} from '@/pages/AutoGenPage/SpectrumTagList/service';

import moment from 'moment';
const { Option } = Select;
import { BooleanFormItem, dealManyToManyFieldTags, fileUpload, twoColumns, richForm, richCol, dealPureSelectField, orderForm, exportExcelCurrent, exportExcelAll, getUpdateColumns, dealRemoveError, dealError, BooleanDisplay, dealDateTimeDisplay, dealManyToManyField, dealTime, deepCopy, fieldErrorHandle, getTableColumns, renderManyToMany, richTrans, dealForeignKeyField, renderForeignKey, fieldsLevelErrorHandle } from '@/utils/utils';
import 'braft-editor/dist/index.css'
const FormItem = Form.Item;
const TableList = () => {
  const [createModalVisible, handleModalVisible] = useState(false);
  const [updateModalVisible, handleUpdateModalVisible] = useState(false);
 
  const [updateFormValues, setUpdateFormValues] = useState({});
  const actionRef = useRef();
  const addFormRef = useRef();
  const updateFormRef = useRef();

  const handleAdd = async fields => {
    const hide = message.loading('正在添加');

    try {
      await addSpectrum({ ...fields });
      hide();
      message.success('添加成功');
      return true;
    } catch (error) {
      return dealError(error, addFormRef, hide, "添加");
    }
  };

  const handleUpdate = async (value, current_id) => {
    const hide = message.loading('正在修改');

    try {
      await updateSpectrum(value, current_id);
      hide();
      message.success('修改成功');
      return true;
    } catch (error) {
      return dealError(error, updateFormRef, hide, "修改");
    }
  };

  const handleRemove = async selectedRows => {
    const hide = message.loading('正在删除');
    if (!selectedRows) return true;

    try {
      const ids = selectedRows.map(row => row.id).join(',');
      await removeSpectrum(ids);
      hide();
      message.success('删除成功');
      return true;
    } catch (error) {
      hide()
      return dealRemoveError(error, "删除");
    }
  };
 
  const dateFieldList = ["updated","created"]
  const base_columns = [{
                             title: 'id',
                             
        hideInForm: true,
        hideInSearch: true,
        
                             
                             dataIndex: 'id',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'ordering',
                             
                             initialValue: 0,
                             dataIndex: 'ordering',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'description',
                             
                             initialValue: "",
                             dataIndex: 'description',
                             valueType: 'textarea',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'activated',
                             
                             initialValue: true,
                             dataIndex: 'activated',
                             
                             rules: [
                                     
                             ],
                             
                                     render: (text, record) => {
                                  return BooleanDisplay(text);
                                },
                        renderFormItem: (item, {value, onChange}) => {
                          return BooleanFormItem(value, onChange);
                        },
        
                             
                        },
                      {
                             title: 'deleted',
                             
                             initialValue: false,
                             dataIndex: 'deleted',
                             
                             rules: [
                                     
                             ],
                             
                                     render: (text, record) => {
                                  return BooleanDisplay(text);
                                },
                        renderFormItem: (item, {value, onChange}) => {
                          return BooleanFormItem(value, onChange);
                        },
        
                             
                        },
                      {
                             title: 'updated',
                             
            hideInForm: true,
            
                             
                             dataIndex: 'updated',
                             valueType: 'dateTime',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'created',
                             
                             
                             dataIndex: 'created',
                             valueType: 'dateTime',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'experiment',
                             
                             
                             dataIndex: 'experiment',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'experiment为必填项',
                     },
                             ],
                             
                        renderFormItem: (item, {value, onChange}) => {
                                          return dealForeignKeyField(item, value, onChange, experimentForeignKeyList);
                                  },
                        render: (text, record) => {
                              return renderForeignKey(text, experimentVerboseNameMap);
                            },
                             
                        },
                      {
                             title: 'compound',
                             
                             
                             dataIndex: 'compound',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'compound为必填项',
                     },
                             ],
                             
                        renderFormItem: (item, {value, onChange}) => {
                                          return dealForeignKeyField(item, value, onChange, compoundForeignKeyList);
                                  },
                        render: (text, record) => {
                              return renderForeignKey(text, compoundVerboseNameMap);
                            },
                             
                        },
                      {
                             title: 'precursor_mz',
                             
                             
                             dataIndex: 'precursor_mz',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'precursor_mz为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'method_type',
                             
                             
                             dataIndex: 'method_type',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'method_type为必填项',
                     },
                             ],
                             
                        renderFormItem: (item, {value, onChange}) => {
                                          return dealForeignKeyField(item, value, onChange, method_typeForeignKeyList);
                                  },
                        render: (text, record) => {
                              return renderForeignKey(text, method_typeVerboseNameMap);
                            },
                             
                        },
                      {
                             title: 'polarity',
                             
                             
                             dataIndex: 'polarity',
                             valueType: 'textarea',
                             rules: [
                                     {
                      required: true,
                      message: 'polarity为必填项',
                     },
                             ],
                             
                             valueEnum:{"NEG":"NEG","POS":"POS","ALL":"ALL"}
                        },
                      {
                             title: 'cid_q',
                             
                             
                             dataIndex: 'cid_q',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'cid_q为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'cid_amp',
                             
                             
                             dataIndex: 'cid_amp',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'cid_amp为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'inj_lmco_mz',
                             
                             initialValue: 50,
                             dataIndex: 'inj_lmco_mz',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'iso1_amp',
                             
                             
                             dataIndex: 'iso1_amp',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'iso1_amp为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'iso2_amp',
                             
                             
                             dataIndex: 'iso2_amp',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'iso2_amp为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'average',
                             
                             initialValue: 1,
                             dataIndex: 'average',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'peaks',
                             
                             initialValue: "<class 'dict'>",
                             dataIndex: 'peaks',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'extra_params',
                             
                             initialValue: "<class 'dict'>",
                             dataIndex: 'extra_params',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'precursor_mz_ms3',
                             
                             initialValue: "0",
                             dataIndex: 'precursor_mz_ms3',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'iso_amp_ms3',
                             
                             initialValue: "0",
                             dataIndex: 'iso_amp_ms3',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'cid_amp_ms3',
                             
                             initialValue: "0",
                             dataIndex: 'cid_amp_ms3',
                             
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'scan_mass_start',
                             
                             initialValue: 50,
                             dataIndex: 'scan_mass_start',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'scan_mass_end',
                             
                             initialValue: 1000,
                             dataIndex: 'scan_mass_end',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'spectrum_tag',
                             
                             
                             dataIndex: 'spectrum_tag',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'spectrum_tag为必填项',
                     },
                             ],
                             
                
                renderFormItem: (item, {value, onChange, type, defaultRender}) => {
                      return dealManyToManyField(item, value,onChange,type, spectrum_tagManyToManyList)
                },
               render: (text, record) => {
                    return renderManyToMany(text)
            }, 
        
                             
                        },
                          {
                              title: '操作',
                              dataIndex: 'option',
                              valueType: 'option',
                                    fixed: 'right',
          width: 100,
                              render: (text, record) => (
                                <>

                                  <EditOutlined title="编辑" className="icon" onClick={async () => {
                                   record.updated = record.updated === null ? record.updated : moment(record.updated);record.created = record.created === null ? record.created : moment(record.created);
                                    handleUpdateModalVisible(true);
                                    setUpdateFormValues(record);
                                  }} />
                                  <Divider type="vertical" />
                                  <Popconfirm
                                    title="您确定要删除spectrum吗？"
                                    placement="topRight"
                                    onConfirm={() => {
                                      handleRemove([record])
                                      actionRef.current.reloadAndRest();
                                    }}
                                    okText="确定"
                                    cancelText="取消"
                                  >
                                    <DeleteOutlined title="删除" className="icon" />
                                  </Popconfirm>
                                </>
                              ),
                            },];

  let cp = deepCopy(base_columns);

  const [formOrder, setFormOrder] = useState([]);

  useEffect(() => {
    querySpectrumDisplayOrder().then(r => {
      setFormOrder(r.form_order)
    })
  }, [])
  const table_columns = getTableColumns(cp);

  let order_cp = deepCopy(base_columns);
  const form_ordered = orderForm(formOrder, order_cp);

  const create_columns = [...form_ordered];
  const update_cp = deepCopy(form_ordered)
  const update_columns = getUpdateColumns(update_cp);

  const [columnsStateMap, setColumnsStateMap] = useState({});

  const [paramState, setParamState] = useState({});

  useEffect(() => {
    querySpectrumListDisplay().then(value => {
      setColumnsStateMap(value)
    })
  }, [])


   
                                const [experimentForeignKeyList, setExperimentForeignKeyList] = useState([]);
                                useEffect(() => {
                                queryExperiment({all: 1}).then(value => {
                                     setExperimentForeignKeyList(value);
                                });
                                }, []);
                                const [experimentVerboseNameMap, setExperimentVerboseNameMap] = useState([]);
                                useEffect(() => {
                                queryExperimentVerboseName().then(value => {
                                    setExperimentVerboseNameMap(value);
                                });
                                }, []);
                                const [compoundForeignKeyList, setCompoundForeignKeyList] = useState([]);
                                useEffect(() => {
                                queryCompound({all: 1}).then(value => {
                                     setCompoundForeignKeyList(value);
                                });
                                }, []);
                                const [compoundVerboseNameMap, setCompoundVerboseNameMap] = useState([]);
                                useEffect(() => {
                                queryCompoundVerboseName().then(value => {
                                    setCompoundVerboseNameMap(value);
                                });
                                }, []);
                                const [method_typeForeignKeyList, setMethod_typeForeignKeyList] = useState([]);
                                useEffect(() => {
                                queryMethodType({all: 1}).then(value => {
                                     setMethod_typeForeignKeyList(value);
                                });
                                }, []);
                                const [method_typeVerboseNameMap, setMethod_typeVerboseNameMap] = useState([]);
                                useEffect(() => {
                                queryMethodTypeVerboseName().then(value => {
                                    setMethod_typeVerboseNameMap(value);
                                });
                                }, []);

   const [spectrum_tagManyToManyList, setSpectrum_tagManyToManyList] = useState([]);
                        useEffect(() => {
                          querySpectrumTag({all:1}).then(value => {
                            setSpectrum_tagManyToManyList(value);
                          });
                        }, []);
  return (
    <PageHeaderWrapper>
      <ProTable
        beforeSearchSubmit={(params => {
          dealTime(params, dateFieldList);
          return params;
        })}
        params={paramState}
        scroll={{ x: '100%' }}
        columnsStateMap={columnsStateMap}
        onColumnsStateChange={(map) => setColumnsStateMap(map)}
        headerTitle="spectrum表格"
        actionRef={actionRef}
        rowKey="id"
        toolBarRender={(action, { selectedRows }) => [
          <Button type="primary" onClick={() => handleModalVisible(true)}>
            <PlusOutlined /> 新建
          </Button>,
          <Button type="primary" onClick={() => exportExcelAll(paramState, querySpectrum, table_columns, 'spectrum-All')}>
            <ExportOutlined /> 导出全部
          </Button>,
          <Input.Search style={{ marginRight: 20 }} placeholder="搜索spectrum" onSearch={value => {
            setParamState({
              search: value,
            });
            actionRef.current.reload();
          }} />,
          selectedRows && selectedRows.length > 0 && (
            <Dropdown
              overlay={
                <Menu
                  onClick={async e => {
                    if (e.key === 'remove') {
                      await handleRemove(selectedRows);
                      actionRef.current.reloadAndRest();
                    }
                    else if (e.key === 'export_current') {
                      exportExcelCurrent(selectedRows, table_columns, 'spectrum-select')
                    }
                  }}
                  selectedKeys={[]}
                >
                  <Menu.Item key="remove">批量删除</Menu.Item>
                  <Menu.Item key="export_current">导出已选</Menu.Item>
                </Menu>
              }
            >
              <Button>
                批量操作 <DownOutlined />
              </Button>
            </Dropdown>
          ),
        ]}
        tableAlertRender={({ selectedRowKeys, selectedRows }) => (
          selectedRowKeys.length > 0 ? <div>
            已选择{' '}
            <a
              style={{
                fontWeight: 600,
              }}
            >
              {selectedRowKeys.length}
            </a>{' '}
            项&nbsp;&nbsp;
          </div> : false

        )}
        request={(params, sorter, filter) => querySpectrum({ ...params, sorter, filter })}
        columns={table_columns}
        rowSelection={{}}
      />
      <CreateForm onCancel={() => handleModalVisible(false)} modalVisible={createModalVisible}>
        <ProTable
          formRef={addFormRef}
          onSubmit={async value => {
            richTrans(value);
            const success = await handleAdd(value);

            if (success) {
              handleModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          type="form"
          search={twoColumns}
          form={
            {
              labelCol: { span: 6 },
              labelAlign: 'left',
            }}
          columns={create_columns}
          rowSelection={{}}
        />
      </CreateForm>
      <UpdateForm onCancel={() => handleUpdateModalVisible(false)} modalVisible={updateModalVisible}>
        <ProTable
          formRef={updateFormRef}
          onSubmit={async value => {
            richTrans(value);
            const success = await handleUpdate(value, updateFormValues.id);

            if (success) {
              handleUpdateModalVisible(false);

              if (actionRef.current) {
                actionRef.current.reload();
              }
            }
          }}
          rowKey="key"
          search={twoColumns}
          type="form"
          form={{
            initialValues: updateFormValues, labelCol: { span: 6 },
            labelAlign: 'left',
          }}
          columns={update_columns}
          rowSelection={{}}
        />
      </UpdateForm>
       
    </PageHeaderWrapper>
  );
};

export default TableList;
