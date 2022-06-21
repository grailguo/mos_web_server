import { DeleteOutlined, DownOutlined, EditOutlined, PlusOutlined, ExportOutlined } from '@ant-design/icons';
import { notification, Button, Col, Descriptions, Divider, Dropdown, Form, Input, Menu, message, Popconfirm, Popover, Row, Select, Tag, Transfer, Switch } from 'antd';
import React, { useEffect, useRef, useState } from 'react';
import KeyOutlined from '@ant-design/icons/lib/icons/KeyOutlined';
import { PageHeaderWrapper } from '@ant-design/pro-layout';
import ProTable from 'mtianyan-pro-table';
import CreateForm from './components/CreateForm';
import { addCartridge, queryCartridge, removeCartridge, updateCartridge, queryCartridgeVerboseName, queryCartridgeListDisplay, queryCartridgeDisplayOrder} from './service';
import UpdateForm from './components/UpdateForm';
import UploadAvatar from '@/components/UploadAvatar';
import {querySource, querySourceVerboseName} from '@/pages/AutoGenPage/SourceList/service';import {queryAnalysisType, queryAnalysisTypeVerboseName} from '@/pages/AutoGenPage/AnalysisTypeList/service';import {queryCompound} from '@/pages/AutoGenPage/CompoundList/service';import {queryCompoundTag} from '@/pages/AutoGenPage/CompoundTagList/service';import {queryQuantMethod} from '@/pages/AutoGenPage/QuantMethodList/service';

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
      await addCartridge({ ...fields });
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
      await updateCartridge(value, current_id);
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
      await removeCartridge(ids);
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
                             title: 'code',
                             
                             
                             dataIndex: 'code',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'code为必填项',
                     },
                             ],
                             
                             
                        },
                      {
                             title: 'source',
                             
                             
                             dataIndex: 'source',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'source为必填项',
                     },
                             ],
                             
                        renderFormItem: (item, {value, onChange}) => {
                                          return dealForeignKeyField(item, value, onChange, sourceForeignKeyList);
                                  },
                        render: (text, record) => {
                              return renderForeignKey(text, sourceVerboseNameMap);
                            },
                             
                        },
                      {
                             title: 'analysis_type',
                             
                             
                             dataIndex: 'analysis_type',
                             
                             rules: [
                                     {
                      required: true,
                      message: 'analysis_type为必填项',
                     },
                             ],
                             
                        renderFormItem: (item, {value, onChange}) => {
                                          return dealForeignKeyField(item, value, onChange, analysis_typeForeignKeyList);
                                  },
                        render: (text, record) => {
                              return renderForeignKey(text, analysis_typeVerboseNameMap);
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
                             title: 'pre_spary_time',
                             
                             initialValue: 500,
                             dataIndex: 'pre_spary_time',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'spray_voltage_pos',
                             
                             initialValue: 4500,
                             dataIndex: 'spray_voltage_pos',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'spray_voltage_neg',
                             
                             initialValue: 3000,
                             dataIndex: 'spray_voltage_neg',
                             valueType: 'digit',
                             rules: [
                                     
                             ],
                             
                             
                        },
                      {
                             title: 'compound',
                             
                             
                             dataIndex: 'compound',
                             
                             rules: [
                                     
                             ],
                             
                
                renderFormItem: (item, {value, onChange, type, defaultRender}) => {
                      return dealManyToManyField(item, value,onChange,type, compoundManyToManyList)
                },
               render: (text, record) => {
                    return renderManyToMany(text)
            }, 
        
                             
                        },
                      {
                             title: 'compound_tag',
                             
                             
                             dataIndex: 'compound_tag',
                             
                             rules: [
                                     
                             ],
                             
                
                renderFormItem: (item, {value, onChange, type, defaultRender}) => {
                      return dealManyToManyField(item, value,onChange,type, compound_tagManyToManyList)
                },
               render: (text, record) => {
                    return renderManyToMany(text)
            }, 
        
                             
                        },
                      {
                             title: 'quant_method',
                             
                             
                             dataIndex: 'quant_method',
                             
                             rules: [
                                     
                             ],
                             
                
                renderFormItem: (item, {value, onChange, type, defaultRender}) => {
                      return dealManyToManyField(item, value,onChange,type, quant_methodManyToManyList)
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
                                    title="您确定要删除cartridge吗？"
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
    queryCartridgeDisplayOrder().then(r => {
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
    queryCartridgeListDisplay().then(value => {
      setColumnsStateMap(value)
    })
  }, [])


   
                                const [sourceForeignKeyList, setSourceForeignKeyList] = useState([]);
                                useEffect(() => {
                                querySource({all: 1}).then(value => {
                                     setSourceForeignKeyList(value);
                                });
                                }, []);
                                const [sourceVerboseNameMap, setSourceVerboseNameMap] = useState([]);
                                useEffect(() => {
                                querySourceVerboseName().then(value => {
                                    setSourceVerboseNameMap(value);
                                });
                                }, []);
                                const [analysis_typeForeignKeyList, setAnalysis_typeForeignKeyList] = useState([]);
                                useEffect(() => {
                                queryAnalysisType({all: 1}).then(value => {
                                     setAnalysis_typeForeignKeyList(value);
                                });
                                }, []);
                                const [analysis_typeVerboseNameMap, setAnalysis_typeVerboseNameMap] = useState([]);
                                useEffect(() => {
                                queryAnalysisTypeVerboseName().then(value => {
                                    setAnalysis_typeVerboseNameMap(value);
                                });
                                }, []);

   const [compoundManyToManyList, setCompoundManyToManyList] = useState([]);
                        useEffect(() => {
                          queryCompound({all:1}).then(value => {
                            setCompoundManyToManyList(value);
                          });
                        }, []);const [compound_tagManyToManyList, setCompound_tagManyToManyList] = useState([]);
                        useEffect(() => {
                          queryCompoundTag({all:1}).then(value => {
                            setCompound_tagManyToManyList(value);
                          });
                        }, []);const [quant_methodManyToManyList, setQuant_methodManyToManyList] = useState([]);
                        useEffect(() => {
                          queryQuantMethod({all:1}).then(value => {
                            setQuant_methodManyToManyList(value);
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
        headerTitle="cartridge表格"
        actionRef={actionRef}
        rowKey="id"
        toolBarRender={(action, { selectedRows }) => [
          <Button type="primary" onClick={() => handleModalVisible(true)}>
            <PlusOutlined /> 新建
          </Button>,
          <Button type="primary" onClick={() => exportExcelAll(paramState, queryCartridge, table_columns, 'cartridge-All')}>
            <ExportOutlined /> 导出全部
          </Button>,
          <Input.Search style={{ marginRight: 20 }} placeholder="搜索cartridge" onSearch={value => {
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
                      exportExcelCurrent(selectedRows, table_columns, 'cartridge-select')
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
        request={(params, sorter, filter) => queryCartridge({ ...params, sorter, filter })}
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
