/**
 * 按钮事件绑定
 */
function bind_click4btns() {
    var $btn_add = $('#btn-add'),
        $btn_delete = $('#btn-delete');
    $btn_add.on('click', function() {
        popup_plugin('添加插件');
    });
    $btn_delete.on('click', function() {
        delete_plugin($btn_delete, '确定删除所选的插件吗？', 'delete');
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

function plugin_detail(plugin_id) {
    if(plugin_id) {
        var plugin_item = get_plugin_by_id(plugin_id);
        popup_plugin('插件详情', plugin_item);
    }
}

/**
 * 弹出插件信息编辑对话框
 * @param  {String} box_title 对话框标题
 * @param  {Object} plugin_item 插件信息
 */
function popup_plugin(box_title, plugin_item) {
    bootbox.alert('开发中');
}

function delete_plugin($self, msg, action) {
    if(confirm(msg)) {
        var origin_text = $self.attr('value');
        console.log(msg);
    }
}