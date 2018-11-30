/**
 * 按钮事件绑定
 */
function bind_click4btns() {
    var $btn_add = $('#btn-add'),
        $btn_delete = $('#btn-delete');
    $btn_add.on('click', function() {
        popup_role('添加角色');
    });
    $btn_delete.on('click', function() {
        delete_role($btn_delete, '确定删除所选的角色吗？', 'delete');
    });
}

/**
 * 改变按钮状态
 * @param  {jQuery对象} $tb_obj 表格对象
 */
function change_enable($tb_obj) {
    var $btn_disable = $('#btn-disable'),
        $btn_delete = $('#btn-delete');
    var selection = $tb_obj.bootstrapTable('getSelections');
    if(selection.length > 0) {
        $btn_disable.removeAttr('disabled').prop('disabled', false);
        $btn_delete.removeAttr('disabled').prop('disabled', false);
    }
    else {
        $btn_disable.attr('disabled', 'disabled').prop('disabled', true);
        $btn_delete.attr('disabled', 'disabled').prop('disabled', true);
    }
}

function role_detail(role_id) {
    if(role_id) {
        var role_item = get_role_by_id(role_id);
        popup_role('角色详情', role_item);
    }
}

/**
 * 弹出角色信息编辑对话框
 * @param  {String} box_title 对话框标题
 * @param  {Object} role_item 角色信息
 */
function popup_role(box_title, role_item) {
    bootbox.alert('开发中');
}

function delete_role($self, msg, action) {
    if(confirm(msg)) {
        var origin_text = $self.attr('value');
        console.log(msg);
    }
}