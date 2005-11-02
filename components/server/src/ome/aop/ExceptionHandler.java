/*
 * ome.aop.DaoCleanUpHibernate
 *
 *------------------------------------------------------------------------------
 *
 *  Copyright (C) 2005 Open Microscopy Environment
 *      Massachusetts Institute of Technology,
 *      National Institutes of Health,
 *      University of Dundee
 *
 *
 *
 *    This library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU Lesser General Public
 *    License as published by the Free Software Foundation; either
 *    version 2.1 of the License, or (at your option) any later version.
 *
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *    Lesser General Public License for more details.
 *
 *    You should have received a copy of the GNU Lesser General Public
 *    License along with this library; if not, write to the Free Software
 *    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 *------------------------------------------------------------------------------
 */
package ome.aop;

//Java imports

//Third-party libraries
import java.util.HashSet;
import java.util.Set;

import net.sf.acegisecurity.AuthenticationException;

import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import com.caucho.hessian.client.HessianRuntimeException;
import com.caucho.hessian.io.HessianServiceException;

//Application-internal dependencies
import ome.conditions.RootException;

/** 
 * ExceptionHandler which maps all server-side exceptions to something 
 * @author  Josh Moore &nbsp;&nbsp;&nbsp;&nbsp;
 * 				<a href="mailto:josh.moore@gmx.de">josh.moore@gmx.de</a>
 * @version 1.0 
 * <small>
 * (<b>Internal version:</b> $Rev$ $Date$)
 * </small>
 * @since 1.0
 * @DEV.TODO should possibly move to common!org.ome.omero.aop
 */
public class ExceptionHandler implements MethodInterceptor {

	private static Log log = LogFactory.getLog(ExceptionHandler.class);
	
	private final static Set<Class> declaredExceptions = new HashSet<Class>();

	private final static Set<Class> rootExceptions = new HashSet<Class>();
	
	static{
		declaredExceptions.add(IllegalArgumentException.class);
		rootExceptions.add(RootException.class);
		rootExceptions.add(AuthenticationException.class); // Possibly AcegiSecurityException
	}
	
    /**
     * @see org.aopalliance.intercept.MethodInterceptor#invoke(org.aopalliance.intercept.MethodInvocation)
     */
    public Object invoke(MethodInvocation arg0) throws Throwable {
    	try {
    		Object o = arg0.proceed();
    		return o;
    	} catch (Throwable t) {
    		log.debug("Exception thrown ("+t.getClass()+"):"+t.getMessage());
    		if (filter_p(t)){
    			throw new RootException("Internal server error.",t);//TODO
    		}
    		throw t;
    	}
    }

    protected boolean filter_p(Throwable t){
    	
    	if (null == t){
    		return true;
    	}
    	
    	if (declaredExceptions.contains(t.getClass())) {
			return false;
    	}
    	
    	boolean knownSubclass = false;
    	
    	for (Class c : rootExceptions){
    		if (c.isAssignableFrom(t.getClass())){
    			knownSubclass = true;
    			break;
			}
    	}
    	
    	return ! knownSubclass;
		
    }
    
}
