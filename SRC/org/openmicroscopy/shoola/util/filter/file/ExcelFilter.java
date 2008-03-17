/*
 * org.openmicroscopy.shoola.util.filter.file.ExcelFilter 
 *
 *------------------------------------------------------------------------------
 *  Copyright (C) 2006-2008 University of Dundee. All rights reserved.
 *
 *
 * 	This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *  
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, write to the Free Software Foundation, Inc.,
 *  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 *------------------------------------------------------------------------------
 */
package org.openmicroscopy.shoola.util.filter.file;


//Java imports
import java.io.File;
import javax.swing.filechooser.FileFilter;


//Third-party libraries

//Application-internal dependencies

/** 
 * Filters the <code>Excel</code> files.
 *
 * @author  Jean-Marie Burel &nbsp;&nbsp;&nbsp;&nbsp;
 * <a href="mailto:j.burel@dundee.ac.uk">j.burel@dundee.ac.uk</a>
 * @author Donald MacDonald &nbsp;&nbsp;&nbsp;&nbsp;
 * <a href="mailto:donald@lifesci.dundee.ac.uk">donald@lifesci.dundee.ac.uk</a>
 * @version 3.0
 * <small>
 * (<b>Internal version:</b> $Revision: $Date: $)
 * </small>
 * @since OME3.0
 */
public class ExcelFilter 	
	extends CustomizedFileFilter
{
    
    /** Possible file extension. */
    public static final String  EXCEL = "xls";

    /**
	 * 	Overriden to return the extension of the filter.
	 * 	@see CustomizedFileFilter#getExtension()
	 */
	public String getExtension() { return EXCEL; }
	
    /**
     * Overriden to return the description of the filter.
     * @see FileFilter#getDescription()
     */
    public String getDescription() { return "Microsoft Excel (.xls)"; }
        
    /**
     * Overriden to accept file with the declared file extensions.
     * @see FileFilter#accept(File)
     */
    public boolean accept(File f)
    {
        if (f.isDirectory()) return true;
        String s = f.getName();
        String extension = null;
        int i = s.lastIndexOf('.');
        if (i > 0 && i < s.length()-1)
            extension = s.substring(i+1).toLowerCase();
        if (extension != null)
            return (extension.equals(EXCEL));
        return false;
    }
    
}
