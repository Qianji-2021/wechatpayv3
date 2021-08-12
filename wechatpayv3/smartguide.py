# -*- coding: utf-8 -*-

from .type import RequestType, WeChatPayType


def guides_register(self, corpid, store_id, userid, name, mobile, qr_code, avatar, group_qrcode=None):
    """服务人员注册
    :param corpid: 企业ID, 示例值：'1234567890'
    :param store_id: 门店ID, 示例值：12345678
    :param userid: 企业微信的员工ID, 示例值：'robert'
    :param name: 企业微信的员工姓名, 示例值：'robert'
    :param mobile: 手机号码, 示例值：'13900000000'
    :param qr_code: 员工个人二维码, 示例值：'https://open.work.weixin.qq.com/wwopen/userQRCode?vcode=xxx'
    :param avatar: 头像URL, 示例值：'http://wx.qlogo.cn/mmopen/ajNVdqHZLLA3WJ6DSZUfiakYe37PKnQhBIeOQBO4czqrnZDS79FH5Wm5m4X69TBicnHFlhiafvDwklOpZeXYQQ2icg/0'
    :param group_qrcode: 群二维码URL, 示例值：'http://p.qpic.cn/wwhead/nMl9ssowtibVGyrmvBiaibzDtp/0'
    """
    params = {}
    if corpid:
        params.update({'corpid': corpid})
    else:
        raise Exception('corpid is not assigned.')
    if store_id:
        params.update({'store_id': store_id})
    else:
        raise Exception('store_id is not assigned.')
    if userid:
        params.update({'userid': userid})
    else:
        raise Exception('userid is not assigned.')
    if name:
        params.update({'name': self._core.encrypt(name)})
    else:
        raise Exception('name is not assigned')
    if mobile:
        params.update({'mobile': self._core.encrypt(mobile)})
    else:
        raise Exception('mobile is not assigned.')
    if qr_code:
        params.update({'qr_code': qr_code})
    else:
        raise Exception('qr_code is not assigned.')
    if avatar:
        params.update({'avatar': avatar})
    else:
        raise Exception('avatar is not assigned.')
    if group_qrcode:
        params.update({'group_qrcode': group_qrcode})
    path = '/v3/smartguide/guides'
    return self._core.request(path, method=RequestType.POST, data=params, cipher_data=True)


def guides_assign(self, guide_id, out_trade_no):
    """服务人员分配
    :param guide_id: 服务人员ID，示例值：'LLA3WJ6DSZUfiaZDS79FH5Wm5m4X69TBic'
    :param out_trade_no: 商户订单号, 示例值：'20150806125346'
    """
    params = {}
    if out_trade_no:
        params.update({'out_trade_no': out_trade_no})
    else:
        raise Exception('out_trade_no is not assigned.')
    if not guide_id:
        raise Exception('guide_id is not assigned.')
    path = '/v3/smartguide/guides/%s/assign' % guide_id
    return self._core.request(path, method=RequestType.POST, data=params)

def guides_query(self, store_id, userid=None, mobile=None, work_id=None, limit=None, offset=0):
    """服务人员查询
    :params store_id: 门店ID, 示例值：1234
    :params userid: 企业微信的员工ID, 示例值：'robert'
    :params mobile: 手机号码, 需进行加密处理, 示例值：'7mKQeypi9fKjAggRfvNFPf/bNxPvork4mMVgZkA=='
    :params work_id: 工号, 示例值：'robert'
    :params limit: 最大资源条数, 示例值：5
    :params offset: 请求资源起始位置, 示例值：0
    """
    params = {}
    if not store_id:
        raise Exception('store_id is not assigned.')        
    path = '/v3/smartguide/guides?store_id=%s' % store_id
    if userid:
        path = path + '&userid=%s' % userid
    if mobile:
        path = path + '&mobile=%s' % self._core.encrypt(mobile)
    if work_id:
        path = path + '&work_id=%s' % work_id
    if limit:
        path = path + '&limit=%s' % limit
    if offset:
        path = path + '&offset=%s' % offset
    return self._core.request(path, cipher_data=True)

def guides_update(self, guide_id, name=None, mobile=None, qr_code=None, avatar=None, group_qrcode=None):
    """服务人员信息更新
    :params guide_id: 服务人员ID, 示例值：'LLA3WJ6DSZUfiaZDS79FH5Wm5m4X69TBic'
    :params name: 服务人员姓名, 示例值：'robert'
    :params mobile: 服务人员手机号码, 示例值：'13900000000'
    :params qr_code: 服务人员二维码URL, 示例值：'https://open.work.weixin.qq.com/wwopen/userQRCode?vcode=xxx'
    :params avatar: 服务人员头像URL, 示例值：'http://wx.qlogo.cn/mmopen/ajNVdqHZLLA3WJ6DSZUfiakYe37PKnQhBIeOQBO4czqrnZDS79FH5Wm5m4X69TBicnHFlhiafvDwklOpZeXYQQ2icg/0'
    :params group_qrcode: 群二维码URL, 示例值：'http://p.qpic.cn/wwhead/nMl9ssowtibVGyrmvBiaibzDtp/0'
    """
    params = {}
    if not guide_id:
        raise Exception('guide_id is not assigned.')
    path = '/v3/smartguide/guides/%s' % guide_id
    if name:
        params.update({'name': self._core.encrypt(name)})
    if mobile:
        params.update({'mobile': self._core.encrypt(mobile)})
    if qr_code:
        params.update({'qr_code': qr_code})
    if avatar:
        params.update({'avatar': avatar})
    if group_qrcode:
        params.update({'group_qrcode': group_qrcode})                                
    return self._core.request(path, method=RequestType.PATCH, data=params, cipher_data=True)