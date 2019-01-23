# -----------------------------------------------------------------------------
# This file is part of EventsRecorder
#       https://github.com/ALBA-Synchrotron/EventsRecorder
#
# Copyright 2019 CELLS / ALBA Synchrotron, Bellaterra, Spain
#
# Distributed under the terms of the GNU General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
#
# You should have received a copy of the GNU General Public License
# along with pyIcePAP. If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------
import logging
import PyTango


class EventsListener(object):
    def __init__(self, log):
        self.log = log

    def push_event(self, event):
        if not event.err:
            if self.log:
                self.log.info(event)
        else:
            e = event.errors[0]
            msg = ('Event error (reason: %s; desc: %s)' % (e.reason, e.desc))
            self.log.error(msg)


class AttributeRegister(object):

    def __init__(self):
        self.log = logging.getLogger('EventRecorder')
        self._attrs = {}
        self._listener = EventsListener(self.log)

    def append(self, attr_name):
        attr_name = attr_name.lower()
        if attr_name in self._attrs:
            return True
        try:
            attr_proxy = PyTango.AttributeProxy(attr_name)
            self._attrs[attr_name] = [attr_proxy]
        except Exception as e:
            self.log.error('Can not create DeviceProxy to {0}. '
                           'Error {1}'.format(attr_name, e))
            return False
        try:
            id = attr_proxy.subscribe_event(PyTango.EventType.CHANGE_EVENT,
                                            self._listener)
            self._attrs[attr_name].append(id)
        except Exception as e:
            self.log.error('Can not subscribe to Change Event to {0}. '
                           'Error {1}'.format(attr_name, e))
            return False
        return True

    def pop(self, attr_name):
        attr_name = attr_name.lower()
        if attr_name not in self._attrs:
            return
        try:
            attr_proxy, id = self._attrs.get(attr_name)
            attr_proxy.unsubscribe_event(id)
        except Exception as e:
            self.log.error('Can not unsubscribe the event {0}. '
                           'Error {1}'.format(attr_name, e))

