import React from 'react'
import { CheckCircle, Circle, Loader2 } from 'lucide-react'

interface ProgressStep {
  id: string
  title: string
  description: string
  status: 'completed' | 'current' | 'pending' | 'error'
}

interface ProgressIndicatorProps {
  steps: ProgressStep[]
}

export const ProgressIndicator: React.FC<ProgressIndicatorProps> = ({
  steps
}) => {
  const getStepIcon = (step: ProgressStep) => {
    if (step.status === 'completed') {
      return <CheckCircle className="w-5 h-5 text-green-500" />
    } else if (step.status === 'current') {
      return <Loader2 className="w-5 h-5 text-blue-500 animate-spin" />
    } else if (step.status === 'error') {
      return <Circle className="w-5 h-5 text-red-500" />
    } else {
      return <Circle className="w-5 h-5 text-gray-300" />
    }
  }

  const getStepColor = (step: ProgressStep) => {
    if (step.status === 'completed') {
      return 'text-green-600'
    } else if (step.status === 'current') {
      return 'text-blue-600'
    } else if (step.status === 'error') {
      return 'text-red-600'
    } else {
      return 'text-gray-400'
    }
  }

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
      <h3 className="text-lg font-medium text-gray-900 mb-4">処理状況</h3>
      
      <div className="space-y-4">
        {steps.map((step, index) => (
          <div key={step.id} className="flex items-start">
            <div className="flex-shrink-0 mr-3">
              {getStepIcon(step)}
            </div>
            <div className="flex-1">
              <div className={`font-medium ${getStepColor(step)}`}>
                {step.title}
              </div>
              <div className="text-sm text-gray-500 mt-1">
                {step.description}
              </div>
              {step.status === 'current' && (
                <div className="mt-2">
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-blue-600 h-2 rounded-full animate-pulse" style={{ width: '60%' }}></div>
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
