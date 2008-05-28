# **********************************************************************
#
# Copyright (c) 2003-2007 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.2.1
# Generated from file `omerofs.ice'

import Ice, IcePy, __builtin__
import Ice_BuiltinSequences_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module monitors
_M_monitors = Ice.openModule('monitors')
__name__ = 'monitors'

if not _M_monitors.__dict__.has_key('MonitorClient'):
    _M_monitors._t_MonitorClient = IcePy.declareClass('::monitors::MonitorClient')
    _M_monitors._t_MonitorClientPrx = IcePy.declareProxy('::monitors::MonitorClient')

if not _M_monitors.__dict__.has_key('MonitorServer'):
    _M_monitors.MonitorServer = Ice.createTempClass()
    class MonitorServer(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_monitors.MonitorServer:
                raise RuntimeError('monitors.MonitorServer is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::monitors::MonitorServer')

        def ice_id(self, current=None):
            return '::monitors::MonitorServer'

        #
        # Operation signatures.
        #
        # def createMonitor(self, pathString, wl, bl, proxy, current=None):
        # def startMonitor(self, id, current=None):
        # def stopMonitor(self, id, current=None):
        # def destroyMonitor(self, id, current=None):
        # def getDirectory(self, id, path, filter, current=None):
        # def getBaseName(self, id, fileId, current=None):
        # def getSize(self, id, fileId, current=None):
        # def getOwner(self, id, fileId, current=None):
        # def getCTime(self, id, fileId, current=None):
        # def getMTime(self, id, fileId, current=None):
        # def getATime(self, id, fileId, current=None):
        # def readBlock(self, id, fileId, offset, size, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_monitors._t_MonitorServer)

        __repr__ = __str__

    _M_monitors.MonitorServerPrx = Ice.createTempClass()
    class MonitorServerPrx(Ice.ObjectPrx):

        def createMonitor(self, pathString, wl, bl, proxy, _ctx=None):
            return _M_monitors.MonitorServer._op_createMonitor.invoke(self, (pathString, wl, bl, proxy), _ctx)

        def startMonitor(self, id, _ctx=None):
            return _M_monitors.MonitorServer._op_startMonitor.invoke(self, (id, ), _ctx)

        def stopMonitor(self, id, _ctx=None):
            return _M_monitors.MonitorServer._op_stopMonitor.invoke(self, (id, ), _ctx)

        def destroyMonitor(self, id, _ctx=None):
            return _M_monitors.MonitorServer._op_destroyMonitor.invoke(self, (id, ), _ctx)

        def getDirectory(self, id, path, filter, _ctx=None):
            return _M_monitors.MonitorServer._op_getDirectory.invoke(self, (id, path, filter), _ctx)

        def getBaseName(self, id, fileId, _ctx=None):
            return _M_monitors.MonitorServer._op_getBaseName.invoke(self, (id, fileId), _ctx)

        def getSize(self, id, fileId, _ctx=None):
            return _M_monitors.MonitorServer._op_getSize.invoke(self, (id, fileId), _ctx)

        def getOwner(self, id, fileId, _ctx=None):
            return _M_monitors.MonitorServer._op_getOwner.invoke(self, (id, fileId), _ctx)

        def getCTime(self, id, fileId, _ctx=None):
            return _M_monitors.MonitorServer._op_getCTime.invoke(self, (id, fileId), _ctx)

        def getMTime(self, id, fileId, _ctx=None):
            return _M_monitors.MonitorServer._op_getMTime.invoke(self, (id, fileId), _ctx)

        def getATime(self, id, fileId, _ctx=None):
            return _M_monitors.MonitorServer._op_getATime.invoke(self, (id, fileId), _ctx)

        def readBlock(self, id, fileId, offset, size, _ctx=None):
            return _M_monitors.MonitorServer._op_readBlock.invoke(self, (id, fileId, offset, size), _ctx)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_monitors.MonitorServerPrx.ice_checkedCast(proxy, '::monitors::MonitorServer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_monitors.MonitorServerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_monitors._t_MonitorServerPrx = IcePy.defineProxy('::monitors::MonitorServer', MonitorServerPrx)

    _M_monitors._t_MonitorServer = IcePy.defineClass('::monitors::MonitorServer', MonitorServer, (), True, None, (), ())
    MonitorServer.ice_type = _M_monitors._t_MonitorServer

    MonitorServer._op_createMonitor = IcePy.Operation('createMonitor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), _M_Ice._t_StringSeq), ((), _M_Ice._t_StringSeq), ((), _M_monitors._t_MonitorClientPrx)), (), IcePy._t_string, ())
    MonitorServer._op_startMonitor = IcePy.Operation('startMonitor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_bool, ())
    MonitorServer._op_stopMonitor = IcePy.Operation('stopMonitor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_bool, ())
    MonitorServer._op_destroyMonitor = IcePy.Operation('destroyMonitor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_bool, ())
    MonitorServer._op_getDirectory = IcePy.Operation('getDirectory', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_string)), (), _M_Ice._t_StringSeq, ())
    MonitorServer._op_getBaseName = IcePy.Operation('getBaseName', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_string, ())
    MonitorServer._op_getSize = IcePy.Operation('getSize', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_long, ())
    MonitorServer._op_getOwner = IcePy.Operation('getOwner', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_string, ())
    MonitorServer._op_getCTime = IcePy.Operation('getCTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_float, ())
    MonitorServer._op_getMTime = IcePy.Operation('getMTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_float, ())
    MonitorServer._op_getATime = IcePy.Operation('getATime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string)), (), IcePy._t_float, ())
    MonitorServer._op_readBlock = IcePy.Operation('readBlock', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_long), ((), IcePy._t_int)), (), _M_Ice._t_ByteSeq, ())

    _M_monitors.MonitorServer = MonitorServer
    del MonitorServer

    _M_monitors.MonitorServerPrx = MonitorServerPrx
    del MonitorServerPrx

if not _M_monitors.__dict__.has_key('MonitorClient'):
    _M_monitors.MonitorClient = Ice.createTempClass()
    class MonitorClient(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_monitors.MonitorClient:
                raise RuntimeError('monitors.MonitorClient is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::monitors::MonitorClient')

        def ice_id(self, current=None):
            return '::monitors::MonitorClient'

        #
        # Operation signatures.
        #
        # def fsEventHappened(self, id, el, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_monitors._t_MonitorClient)

        __repr__ = __str__

    _M_monitors.MonitorClientPrx = Ice.createTempClass()
    class MonitorClientPrx(Ice.ObjectPrx):

        def fsEventHappened(self, id, el, _ctx=None):
            return _M_monitors.MonitorClient._op_fsEventHappened.invoke(self, (id, el), _ctx)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_monitors.MonitorClientPrx.ice_checkedCast(proxy, '::monitors::MonitorClient', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_monitors.MonitorClientPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_monitors._t_MonitorClientPrx = IcePy.defineProxy('::monitors::MonitorClient', MonitorClientPrx)

    _M_monitors._t_MonitorClient = IcePy.defineClass('::monitors::MonitorClient', MonitorClient, (), True, None, (), ())
    MonitorClient.ice_type = _M_monitors._t_MonitorClient

    MonitorClient._op_fsEventHappened = IcePy.Operation('fsEventHappened', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), _M_Ice._t_StringSeq)), (), None, ())

    _M_monitors.MonitorClient = MonitorClient
    del MonitorClient

    _M_monitors.MonitorClientPrx = MonitorClientPrx
    del MonitorClientPrx

# End of module monitors
