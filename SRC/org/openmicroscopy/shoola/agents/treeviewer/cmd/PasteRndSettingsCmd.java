/*
 * org.openmicroscopy.shoola.agents.treeviewer.cmd.PasteRndSettingsCmd 
 *
 *------------------------------------------------------------------------------
 *  Copyright (C) 2006-2007 University of Dundee. All rights reserved.
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
package org.openmicroscopy.shoola.agents.treeviewer.cmd;


//Java imports

//Third-party libraries

//Application-internal dependencies
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

import org.openmicroscopy.shoola.agents.treeviewer.browser.Browser;
import org.openmicroscopy.shoola.agents.treeviewer.browser.TreeImageDisplay;
import org.openmicroscopy.shoola.agents.treeviewer.browser.TreeImageTimeSet;
import org.openmicroscopy.shoola.agents.treeviewer.view.TreeViewer;
import org.openmicroscopy.shoola.env.data.model.TimeRefObject;

import pojos.DataObject;
import pojos.ExperimenterData;
import pojos.ImageData;

/** 
 * Pastes the rendering settings across the collection of images.
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
public class PasteRndSettingsCmd 
	implements ActionCmd
{

	/** Reference to the model. */
    private TreeViewer model;
    
    /**
     * Creates a new instance.
     * 
     * @param model Reference to the model. Mustn't be <code>null</code>.
     */
    public PasteRndSettingsCmd(TreeViewer model)
    {
        if (model == null) throw new IllegalArgumentException("No model.");
        this.model = model;
    }
    
    /** Implemented as specified by {@link ActionCmd}. */
    public void execute()
    {
    	if (!model.hasRndSettings()) return;
    	Browser b = model.getSelectedBrowser();
		if (b == null) return;
		TreeImageDisplay[] nodes = b.getSelectedDisplays();
		if (nodes.length == 0) return; 
		TreeImageDisplay node;
		TreeImageTimeSet time;
		Set<Long> ids = new HashSet<Long>();
		Class klass = null;
		Object ho;
		Iterator j;
		ExperimenterData exp;
		TimeRefObject ref = null;
		for (int i = 0; i < nodes.length; i++) {
			node = nodes[i];
			if (node instanceof TreeImageTimeSet) {
				if (node.containsImages()) {
					klass = ImageData.class;
					j = ViewCmd.getImageNodeIDs(node, b).iterator();
					while (j.hasNext())
						ids.add((Long) j.next());
				} else {
					time = (TreeImageTimeSet) node;
            		int c = ViewCmd.getTimeConstrain(time.getType());
            		exp = model.getUserDetails();
            		ref = new TimeRefObject(exp.getId(), 
            				time.getLowerTime(), time.getTime(), c);
				}
			} else {
				ho = node.getUserObject();
				klass = ho.getClass();
				if (ho instanceof DataObject) {
					ids.add(((DataObject) ho).getId());
				}
			}
		}
		if (ref != null) model.pasteRndSettings(ref);
		else model.pasteRndSettings(ids, klass);
    }
    
}
