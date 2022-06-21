[
    {
        name: 'Home',
        path: '/xadmin/index',
        icon: 'dashboard',
        component: './TyAdminBuiltIn/DashBoard'
    },
    {
        path: '/xadmin/',
        redirect: '/xadmin/index',
    },
    {
        name: 'Authentication and Authorization',
        icon: 'BarsOutlined',
        path: '/xadmin/auth',
        routes:
        [
            {
                name: 'permission',
                path: '/xadmin/auth/permission',
                component: './AutoGenPage/PermissionList',
            },
            {
                name: 'group',
                path: '/xadmin/auth/group',
                component: './AutoGenPage/GroupList',
            }
        ]
    },
    {
        name: 'Erecto',
        icon: 'BarsOutlined',
        path: '/xadmin/erecto',
        routes:
        [
            {
                name: 'method type',
                path: '/xadmin/erecto/method_type',
                component: './AutoGenPage/MethodTypeList',
            },
            {
                name: 'analysis type',
                path: '/xadmin/erecto/analysis_type',
                component: './AutoGenPage/AnalysisTypeList',
            },
            {
                name: 'matrix',
                path: '/xadmin/erecto/matrix',
                component: './AutoGenPage/MatrixList',
            },
            {
                name: 'source',
                path: '/xadmin/erecto/source',
                component: './AutoGenPage/SourceList',
            },
            {
                name: 'eluent',
                path: '/xadmin/erecto/eluent',
                component: './AutoGenPage/EluentList',
            },
            {
                name: 'unit',
                path: '/xadmin/erecto/unit',
                component: './AutoGenPage/UnitList',
            },
            {
                name: 'conc unit',
                path: '/xadmin/erecto/conc_unit',
                component: './AutoGenPage/ConcUnitList',
            }
        ]
    },
    {
        name: 'Reparo',
        icon: 'BarsOutlined',
        path: '/xadmin/reparo',
        routes:
        [
            {
                name: 'device',
                path: '/xadmin/reparo/device',
                component: './AutoGenPage/DeviceList',
            }
        ]
    },
    {
        name: 'Accio',
        icon: 'BarsOutlined',
        path: '/xadmin/accio',
        routes:
        [
            {
                name: 'compound code counter',
                path: '/xadmin/accio/compound_code_counter',
                component: './AutoGenPage/CompoundCodeCounterList',
            },
            {
                name: 'compound tag',
                path: '/xadmin/accio/compound_tag',
                component: './AutoGenPage/CompoundTagList',
            },
            {
                name: 'compound',
                path: '/xadmin/accio/compound',
                component: './AutoGenPage/CompoundList',
            },
            {
                name: 'experiment',
                path: '/xadmin/accio/experiment',
                component: './AutoGenPage/ExperimentList',
            },
            {
                name: 'spectrum tag',
                path: '/xadmin/accio/spectrum_tag',
                component: './AutoGenPage/SpectrumTagList',
            },
            {
                name: 'spectrum',
                path: '/xadmin/accio/spectrum',
                component: './AutoGenPage/SpectrumList',
            },
            {
                name: 'quant method code counter',
                path: '/xadmin/accio/quant_method_code_counter',
                component: './AutoGenPage/QuantMethodCodeCounterList',
            },
            {
                name: 'quant method',
                path: '/xadmin/accio/quant_method',
                component: './AutoGenPage/QuantMethodList',
            },
            {
                name: 'cartridge',
                path: '/xadmin/accio/cartridge',
                component: './AutoGenPage/CartridgeList',
            }
        ]
    },
    {
        name: 'TyadminBuiltin',
        icon: 'VideoCamera',
        path: '/xadmin/sys',
        routes:
        [
            {
                name: 'TyAdminLog',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_sys_log',
                component: './TyAdminBuiltIn/TyAdminSysLogList'
            },
            {
                name: 'TyAdminVerify',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_email_verify_record',
                component: './TyAdminBuiltIn/TyAdminEmailVerifyRecordList'
            }
        ]
    },
    {
        name: 'passwordModify',
        path: '/xadmin/account/change_password',
        hideInMenu: true,
        icon: 'dashboard',
        component: './TyAdminBuiltIn/ChangePassword',
    },
    {
        component: './404',
    },
]
